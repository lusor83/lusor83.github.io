import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

SCRIPT = Path(__file__).resolve().parents[2] / "tools" / "kinetidrop-distribution" / "prepare.py"
SPEC = importlib.util.spec_from_file_location("kinetidrop_prepare", SCRIPT)
prepare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prepare)


class PrepareTests(unittest.TestCase):
    def test_safe_extract_rejects_zip_slip(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "unsafe.zip"
            with ZipFile(source, "w") as archive:
                archive.writestr("../escaped.txt", "bad")
            with self.assertRaises(ValueError):
                prepare.safe_extract(source, Path(tmp) / "out")

    def test_inspect_and_candidate_packaging(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            (root / "textures").mkdir(parents=True)
            (root / "scene.blend").write_bytes(b"test-placeholder")
            (root / "textures" / "albedo.png").write_bytes(b"test-placeholder")
            out = Path(tmp) / "out"
            prepare.inspect(root, out)
            inventory = json.loads((out / "inventory.json").read_text(encoding="utf-8"))
            self.assertEqual(inventory["file_count"], 2)
            self.assertEqual(len(inventory["blend_files"]), 1)
            prepare.prep_asset(root, out)
            target = out / "blender_pack_candidate.zip"
            self.assertTrue(target.exists())
            with ZipFile(target) as archive:
                self.assertIn("source/scene.blend", archive.namelist())
                self.assertIn("source/textures/albedo.png", archive.namelist())
                self.assertIn("README_DRAFT.md", archive.namelist())
                self.assertIn("FILE_MANIFEST.json", archive.namelist())

    def test_asset_pack_requires_blend(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            root.mkdir()
            with self.assertRaises(RuntimeError):
                prepare.prep_asset(root, Path(tmp) / "out")


if __name__ == "__main__":
    unittest.main()
