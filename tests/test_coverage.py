"""Coverage tests: page map and example inventory must be complete."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestCoverage(unittest.TestCase):
    def test_page_map_covers_all_pages(self):
        text = (ROOT / "references/cakupan-halaman.md").read_text(encoding="utf-8")
        pages = [int(n) for n in re.findall(r"(?m)^\| (\d+) \|", text)]
        self.assertEqual(pages, list(range(1, 35)))

    def test_36_topics_and_9_appendices(self):
        text = (ROOT / "references/contoh-dan-lampiran.md").read_text(encoding="utf-8")
        topics, appendices = text.split("## Lampiran resmi", 1)
        self.assertEqual(
            [int(n) for n in re.findall(r"(?m)^(\d+)\. ", topics)],
            list(range(1, 37)),
        )
        self.assertEqual(
            [int(n) for n in re.findall(r"(?m)^(\d+)\. ", appendices)],
            list(range(1, 10)),
        )

    def test_conflicts_documented(self):
        text = (ROOT / "references/ketidakselarasan.md").read_text(encoding="utf-8")
        self.assertIn("21,5 cm", text)


if __name__ == "__main__":
    unittest.main()
