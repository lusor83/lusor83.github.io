"""Pack linked images into a *copy* of a Blender scene; run from Blender 3.6+.

Example (Windows):
  blender -b original.blend --python blender_pack.py -- --out packed_copy.blend

Do not assume stock/commercial redistribution rights from a successful pack.
"""
import argparse
import json
import os
from pathlib import Path
import sys

import bpy


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    output = Path(args.out).expanduser().resolve()
    original = Path(bpy.data.filepath).resolve() if bpy.data.filepath else None
    if original is None or not original.exists():
        raise RuntimeError("No saved Blender .blend scene loaded")
    if output == original:
        raise RuntimeError("Output must be different from the original scene")
    if output.exists():
        raise RuntimeError(f"Refusing to overwrite existing output: {output}")
    missing = []
    for img in bpy.data.images:
        if img.source != "FILE" or img.packed_file:
            continue
        p = bpy.path.abspath(img.filepath, library=img.library)
        if not os.path.isfile(p):
            missing.append({"image": img.name, "path": p})
    if missing:
        print(json.dumps({"missing_images": missing}, indent=2))
        raise RuntimeError("Missing source image(s); fix paths before packaging")
    bpy.ops.file.pack_all()
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(output), check_existing=False)
    report = {"original": str(original), "output": str(output),
              "packed_images": sum(bool(x.packed_file) for x in bpy.data.images),
              "note": "Commercial rights, render quality and external linked libraries not certified"}
    output.with_suffix(".pack-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
