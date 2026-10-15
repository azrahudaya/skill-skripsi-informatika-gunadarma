"""Test unit untuk scripts/audit_skripsi.py."""

from pathlib import Path
import tempfile
import unittest

from scripts.audit_skripsi import audit_manuscript, extract_text_from_plain, extract_text_from_tex

SAMPLE_TEXT = """# SKRIPSI INFORMATIKA GUNADARMA

## Abstrak
Ini adalah ringkasan penelitian yang dibuat singkat dan padat untuk menguji batas kata.

## Abstract
This is an English abstract sample to test word limits and structure.

1. PENDAHULUAN

1.1 Latar Belakang
Paragraf pertama latar belakang menjelaskan masalah komputasi yang dihadapi mahasiswa Informatika.

Paragraf kedua menjelaskan perlunya otomatisasi dan verifikasi mandiri berbasis aturan pedoman 2025.

Paragraf ketiga merangkum solusi inovatif yang diajukan beserta keunggulannya.

1.2 Rumusan Masalah
Paragraf tunggal yang sengaja dibuat kurang dari tiga paragraf untuk menguji deteksi subbab pendek.

1.3 Tujuan Penelitian
Tujuan pertama dari penelitian ini.

Tujuan kedua dari penelitian ini.

Tujuan ketiga dari penelitian ini.

2. TINJAUAN PUSTAKA
Paragraf 1 tinjauan pustaka.
Paragraf 2 tinjauan pustaka.
Paragraf 3 tinjauan pustaka.

3. METODE PENELITIAN
Paragraf 1 metode penelitian.
Paragraf 2 metode penelitian.
Paragraf 3 metode penelitian.

4. HASIL DAN PEMBAHASAN
Paragraf 1 hasil dan pembahasan.
Paragraf 2 hasil dan pembahasan.
Paragraf 3 hasil dan pembahasan.

5. PENUTUP
5.1 Kesimpulan
Kesimpulan 1 menjawab rumusan masalah.
Kesimpulan 2 menjawab tujuan.
Kesimpulan 3 memberikan ringkasan kontribusi.

DAFTAR PUSTAKA
Ahmad, F. 2024. Penerapan Machine Learning. Jurnal Informatika, 10(2), 12-20. doi:10.1234/ji.2024.01
Budi, S. 2023. Deep Learning Architecture. IEEE Trans on AI, 5(1), 40-50. doi:10.1109/TAI.2023.12
"""


class TestAuditScript(unittest.TestCase):
    def test_audit_logic(self):
        with tempfile.NamedTemporaryFile("w+", suffix=".md", delete=False) as tf:
            tf.write(SAMPLE_TEXT)
            tf_path = Path(tf.name)

        try:
            paras = extract_text_from_plain(tf_path)
            report = audit_manuscript(paras)

            # Cek 5 bab (dengan format 1. PENDAHULUAN tanpa kata BAB)
            self.assertTrue(report["bab_checks"]["Bab 1 Pendahuluan"])
            self.assertTrue(report["bab_checks"]["Bab 2 Tinjauan Pustaka"])
            self.assertTrue(report["bab_checks"]["Bab 3 Metode Penelitian"])
            self.assertTrue(report["bab_checks"]["Bab 4 Hasil dan Pembahasan"])
            self.assertTrue(report["bab_checks"]["Bab 5 Penutup"])

            # Cek subbab pendek terdeteksi
            short_titles = [s["title"] for s in report["short_subsections"]]
            self.assertTrue(any("1.2" in t for t in short_titles))

            # Cek abstrak
            self.assertGreater(report["abstract_counts"]["indonesia_words"], 0)
            self.assertLessEqual(report["abstract_counts"]["indonesia_words"], 250)

            # Cek daftar pustaka terdeteksi DOI
            self.assertGreaterEqual(report["bibliography"]["doi_count"], 1)

        finally:
            if tf_path.is_file():
                tf_path.unlink()

    def test_latex_modular_and_bib(self):
        with tempfile.TemporaryDirectory() as td:
            dir_path = Path(td)
            ch_dir = dir_path / "chapters"
            ch_dir.mkdir()

            bab1 = ch_dir / "bab1.tex"
            bab1.write_text(r"""
            \chapter{1. Pendahuluan}
            \section{1.1 Latar Belakang}
            Paragraf 1 dalam bab 1.

            Paragraf 2 dalam bab 1.

            Paragraf 3 dalam bab 1.
            """, encoding="utf-8")

            bib = dir_path / "daftar-pustaka.bib"
            bib.write_text(r"""
            @article{andi2024,
              author = {Andi, B.},
              title = {Riset Informatika},
              journal = {Jurnal Gunadarma},
              year = {2024},
              doi = {10.1234/gundar.2024}
            }
            """, encoding="utf-8")

            main = dir_path / "main.tex"
            main.write_text(r"""
            \documentclass{report}
            \addbibresource{daftar-pustaka.bib}
            \begin{document}
            \input{chapters/bab1}
            \end{document}
            """, encoding="utf-8")

            paras = extract_text_from_tex(main)
            self.assertTrue(any("1. Pendahuluan" in p["text"] for p in paras))
            self.assertTrue(any("DAFTAR PUSTAKA" in p["text"] for p in paras))
            report = audit_manuscript(paras)
            self.assertTrue(report["bab_checks"]["Bab 1 Pendahuluan"])
            self.assertEqual(report["bibliography"]["total_detected"], 1)
            self.assertEqual(report["bibliography"]["doi_count"], 1)


if __name__ == "__main__":
    unittest.main()
