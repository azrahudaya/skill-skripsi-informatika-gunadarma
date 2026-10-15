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

# BAB 1 PENDAHULUAN

## 1.1 Latar Belakang
Paragraf pertama latar belakang menjelaskan masalah komputasi yang dihadapi mahasiswa Informatika.

Paragraf kedua menjelaskan perlunya otomatisasi dan verifikasi mandiri berbasis aturan pedoman 2025.

Paragraf ketiga merangkum solusi inovatif yang diajukan beserta keunggulannya.

## 1.2 Rumusan Masalah
Paragraf tunggal yang sengaja dibuat kurang dari tiga paragraf untuk menguji deteksi subbab pendek.

## 1.3 Tujuan Penelitian
Tujuan pertama dari penelitian ini.

Tujuan kedua dari penelitian ini.

Tujuan ketiga dari penelitian ini.

# BAB 2 TINJAUAN PUSTAKA
Paragraf 1 tinjauan pustaka.
Paragraf 2 tinjauan pustaka.
Paragraf 3 tinjauan pustaka.

# BAB 3 METODE PENELITIAN
Paragraf 1 metode penelitian.
Paragraf 2 metode penelitian.
Paragraf 3 metode penelitian.

# BAB 4 HASIL DAN PEMBAHASAN
Paragraf 1 hasil dan pembahasan.
Paragraf 2 hasil dan pembahasan.
Paragraf 3 hasil dan pembahasan.

# BAB 5 PENUTUP
## 5.1 Kesimpulan
Kesimpulan 1 menjawab rumusan masalah.
Kesimpulan 2 menjawab tujuan.
Kesimpulan 3 memberikan ringkasan kontribusi.

# DAFTAR PUSTAKA
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

            # Cek 5 bab
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

    def test_latex_extraction(self):
        tex_sample = r"""
        \chapter{BAB 1 PENDAHULUAN}
        \section{1.1 Latar Belakang}
        Paragraf pertama dalam latex.

        Paragraf kedua dalam latex.

        Paragraf ketiga dalam latex.
        """
        with tempfile.NamedTemporaryFile("w+", suffix=".tex", delete=False) as tf:
            tf.write(tex_sample)
            tf_path = Path(tf.name)

        try:
            paras = extract_text_from_tex(tf_path)
            self.assertTrue(any(p["style"] == "Heading1" for p in paras))
            self.assertTrue(any(p["style"] == "Heading2" for p in paras))
            self.assertGreaterEqual(len(paras), 4)
        finally:
            if tf_path.is_file():
                tf_path.unlink()


if __name__ == "__main__":
    unittest.main()
