#!/usr/bin/env python3
"""Inspect and prepare *candidates* for KinetiDrop stock footage and itch.io assets.

Never publishes, alters originals, asserts rights, or creates real stock metadata
without review. Uses the Python standard library; stock mode requires ffmpeg/ffprobe.
"""
from __future__ import annotations
import argparse
import collections
import csv
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile

VIDEO_EXT = {".mp4", ".mov", ".mkv"}
TEXTURE_EXT = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".exr", ".hdr", ".webp", ".svg"}
LIMIT_FILES = 30000
LIMIT_UNCOMPRESSED = 16 * 1024 * 1024 * 1024


def safe_extract(zip_path: Path, destination: Path) -> None:
    with ZipFile(zip_path) as archive:
        entries = archive.infolist()
        if len(entries) > LIMIT_FILES or sum(e.file_size for e in entries) > LIMIT_UNCOMPRESSED:
            raise ValueError("Archive exceeds conservative extraction limits")
        for e in entries:
            rel = PurePosixPath(e.filename.replace("\\", "/"))
            if not rel.parts or rel.is_absolute() or ".." in rel.parts:
                raise ValueError(f"Unsafe ZIP entry: {e.filename}")
            target = destination.joinpath(*rel.parts)
            if e.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            if (e.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError(f"Symlink in archive refused: {e.filename}")
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(e) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst, 1024 * 1024)


def sources(source: Path, tmp: Path) -> Path:
    if source.is_dir():
        return source.resolve()
    if source.is_file() and source.suffix.lower() == ".zip":
        root = tmp / "input"
        root.mkdir()
        safe_extract(source, root)
        return root
    raise ValueError("Source must be an existing folder or .zip archive")


def manifest(root: Path) -> list[dict]:
    output = []
    for f in sorted(root.rglob("*")):
        if f.is_file():
            output.append({"path": str(f.relative_to(root)), "bytes": f.stat().st_size,
                           "extension": f.suffix.lower()})
    return output


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (slug or "untitled")[:65]


def inspect(root: Path, out: Path) -> None:
    items = manifest(root)
    counts = collections.Counter(i["extension"] for i in items)
    details = {"file_count": len(items), "extensions": dict(counts),
               "large_files": sorted(items, key=lambda i: -i["bytes"])[:30],
               "blend_files": [i["path"] for i in items if i["extension"] == ".blend"],
               "videos": [i["path"] for i in items if i["extension"] in VIDEO_EXT]}
    out.mkdir(parents=True, exist_ok=True)
    (out / "inventory.json").write_text(json.dumps(details, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"file_count": len(items), "blend_files": len(details["blend_files"]),
                      "videos": len(details["videos"])}, indent=2))


def probe_video(file: Path) -> dict:
    if not shutil.which("ffprobe"):
        raise RuntimeError("ffprobe not found. Install FFmpeg on PATH first.")
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration:stream=codec_type,width,height,r_frame_rate",
                             "-of", "json", str(file)], capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    video = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
    return {"duration": float(info.get("format", {}).get("duration", 0)),
            "width": video.get("width", 0), "height": video.get("height", 0),
            "fps": video.get("r_frame_rate", "")}


def prep_stock(root: Path, out: Path) -> None:
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise RuntimeError("FFmpeg and ffprobe must be available on PATH")
    dest = out / "stock_candidates"
    dest.mkdir(parents=True, exist_ok=True)
    rows = []
    for n, original in enumerate(sorted(f for f in root.rglob("*") if f.suffix.lower() in VIDEO_EXT), 1):
        rel = original.relative_to(root)
        record = {"source": str(rel), "file": "", "duration_s": "",
                  "width": "", "height": "", "review_status": "SKIPPED",
                  "reason": "", "title_draft": original.stem.replace("_", " ").replace("-", " "),
                  "keywords_draft": "", "rights_verified": "NO"}
        try:
            data = probe_video(original)
            record.update({"duration_s": round(data["duration"], 3),
                           "width": data["width"], "height": data["height"]})
            if not 5 <= data["duration"] <= 60:
                record["reason"] = "Outside target 5-60 second window; edit a distinct clip manually"
            elif min(data["width"], data["height"]) < 1080 or max(data["width"], data["height"]) < 1920:
                record["reason"] = "Below chosen conservative 1080p target; check platform policy"
            else:
                filename = f"{n:03d}_{slugify(original.stem)}.mp4"
                output = dest / filename
                subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                                "-i", str(original), "-map", "0:v:0", "-an",
                                "-c:v", "libx264", "-preset", "medium", "-crf", "16",
                                "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                                str(output)], check=True)
                record["file"] = filename
                record["review_status"] = "TECHNICAL_CANDIDATE_ONLY"
                record["reason"] = "Review content, rights, visual quality, metadata and platform rules"
        except Exception as exc:
            record["reason"] = f"{type(exc).__name__}: {exc}"
        rows.append(record)
    columns = ["source", "file", "duration_s", "width", "height", "review_status",
               "reason", "title_draft", "keywords_draft", "rights_verified"]
    with (out / "stock_review.csv").open("w", newline="", encoding="utf-8-sig") as fp:
        writer = csv.DictWriter(fp, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Stock technical candidates: {sum(x['review_status']=='TECHNICAL_CANDIDATE_ONLY' for x in rows)}/{len(rows)}")
    print(f"Review manifest: {out / 'stock_review.csv'}")


def prep_asset(root: Path, out: Path) -> None:
    blends = sorted(f for f in root.rglob("*.blend") if f.is_file())
    if not blends:
        raise RuntimeError("No .blend found: cannot create Blender asset pack")
    target = out / "blender_pack_candidate.zip"
    target.parent.mkdir(parents=True, exist_ok=True)
    files = sorted({*blends, *(f for f in root.rglob("*") if f.is_file() and f.suffix.lower() in TEXTURE_EXT)})
    draft = (
        "# Blender Scene Asset Pack — DRAFT\n\n"
        "Includes source scenes and discovered texture files. Not ready for sale until checked.\n\n"
        "## Buyer requirements\n"
        "- Open with a compatible Blender version (verify with actual scene).\n"
        "- Verify linked files, packed images, modifiers, materials and animations.\n\n"
        "## Mandatory creator checklist\n"
        "- [ ] Open every scene in Blender on a clean machine.\n"
        "- [ ] Pack all external dependencies and confirm textures render correctly.\n"
        "- [ ] Confirm commercial rights to every element, font, texture and source.\n"
        "- [ ] Remove non-redistributable audio, brands and third-party material.\n"
        "- [ ] Add original preview renders, realistic screenshots and a final license.\n"
        "- [ ] Verify file size and product page description; set price manually.\n"
    )
    with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=6) as archive:
        for f in files:
            archive.write(f, f"source/{f.relative_to(root).as_posix()}")
        archive.writestr("README_DRAFT.md", draft)
        archive.writestr("FILE_MANIFEST.json", json.dumps(
            [{"file": f.relative_to(root).as_posix(), "bytes": f.stat().st_size} for f in files],
            indent=2, ensure_ascii=False))
    print(f"Prepared {target} ({len(blends)} .blend files and {len(files)} files total); NOT sale-ready")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["inspect", "stock", "asset"])
    parser.add_argument("--source", type=Path, required=True, help="ZIP archive or extracted folder")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="kinetidrop-prep-") as temp:
        root = sources(args.source.expanduser(), Path(temp))
        {"inspect": inspect, "stock": prep_stock, "asset": prep_asset}[args.mode](root, args.out)
    print("No uploads performed. Nothing was published or submitted to a marketplace.")


if __name__ == "__main__":
    main()
