"""Package integrity tests (mirror of scripts/validate.py checks)."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestPackage(unittest.TestCase):
    def setUp(self):
        self.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    def test_frontmatter_name(self):
        self.assertTrue(self.skill.startswith("---\n"))
        front = self.skill[4:].split("\n---\n", 1)[0]
        self.assertIn("name: skill-skripsi-informatika-gunadarma", front)
        self.assertIn("description:", front)

    def test_all_references_exist(self):
        import re

        refs = set(re.findall(r"`(references/[^`]+\.md)`", self.skill))
        self.assertEqual(len(refs), 19)
        for rel in refs:
            self.assertTrue((ROOT / rel).is_file(), f"missing {rel}")

    def test_no_local_paths(self):
        import re

        for md in ROOT.rglob("*.md"):
            text = md.read_text(encoding="utf-8")
            self.assertIsNone(
                re.search(r"/home/[^/\s]+/", text), f"local path in {md}"
            )

    def test_no_pdf_committed(self):
        self.assertEqual(list(ROOT.rglob("*.pdf")), [])


if __name__ == "__main__":
    unittest.main()
