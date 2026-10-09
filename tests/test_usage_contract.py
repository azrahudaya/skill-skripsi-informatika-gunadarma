"""Contract tests: the skill must state the key Skripsi-specific rules."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")


class TestUsageContract(unittest.TestCase):
    def test_five_chapters(self):
        for bab in ("Pendahuluan", "Tinjauan Pustaka", "Metode Penelitian",
                    "Hasil dan Pembahasan", "Penutup"):
            self.assertIn(bab, SKILL, f"missing chapter: {bab}")

    def test_minimum_sources(self):
        self.assertIn("20 sumber", SKILL)
        self.assertIn("70% artikel ilmiah", SKILL)

    def test_abstract_limit(self):
        self.assertIn("250 kata", SKILL)

    def test_harvard_and_doi(self):
        self.assertIn("Harvard", SKILL)
        self.assertIn("DOI", SKILL)

    def test_out_of_scope_notes_defense(self):
        self.assertIn("Di luar cakupan", SKILL)
        self.assertIn("sidang", SKILL.lower())

    def test_three_paragraph_rule(self):
        self.assertIn("tiga paragraf", SKILL)


if __name__ == "__main__":
    unittest.main()
