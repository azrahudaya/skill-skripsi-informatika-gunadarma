#!/usr/bin/env python3
"""Pemeriksa dan validator struktur berkas upload repositori perpustakaan Gunadarma (GDLib).

Memeriksa apakah berkas skripsi yang telah dipecah memenuhi konvensi penamaan baku 01 sampai 19.
Hanya menggunakan modul bawaan Python (stdlib: argparse, pathlib, sys).
"""

# ponytail: skrip ini memvalidasi kelengkapan berkas GDLib berbasis konvensi penamaan resmi;
# batasan: pemisahan otomatis halaman PDF bergantung pada poppler-utils (pdfseparate) atau pypdf.

import argparse
from pathlib import Path
import sys

REQUIRED_GDLIB_FILES = [
    ("01_COVER_PENULISAN.pdf", "Halaman Judul dan Sampul Luar"),
    ("02_PERNYATAAN_ORIGINALITAS_PUBLIKASI.pdf", "Lembar Pernyataan Orisinalitas Bermeterai"),
    ("03_PARAF_STEMPEL_LEMBAR_PENGESAHAN.pdf", "Lembar Pengesahan Berstempel Resmi"),
    ("04_ABSTRAKSI_BAHASA_INDONESIA.pdf", "Abstrak Bahasa Indonesia"),
    ("05_ABSTRAKSI_BAHASA_INGGRIS.pdf", "Abstract Bahasa Inggris"),
    ("06_KATA_PENGANTAR.pdf", "Kata Pengantar Lengkap"),
    ("07_DAFTAR_ISI.pdf", "Daftar Isi"),
    ("08_DAFTAR_TABEL.pdf", "Daftar Tabel"),
    ("09_DAFTAR_GAMBAR.pdf", "Daftar Gambar"),
    ("10_DAFTAR_LAMPIRAN.pdf", "Daftar Lampiran (bila ada lampiran)"),
    ("11_BAB_I.pdf", "Bab 1 Pendahuluan"),
    ("12_BAB_II.pdf", "Bab 2 Tinjauan Pustaka"),
    ("13_BAB_III.pdf", "Bab 3 Metode Penelitian"),
    ("14_BAB_IV.pdf", "Bab 4 Hasil dan Pembahasan"),
    ("15_BAB_V.pdf", "Bab 5 Penutup"),
    ("16_DAFTAR_PUSTAKA.pdf", "Daftar Pustaka"),
    ("17_LAMPIRAN.pdf", "Lampiran Kode dan Data"),
    ("18_MANUAL_BOOK.pdf", "Manual Book Petunjuk Sistem"),
    ("19_JURNAL.pdf", "Artikel Ilmiah 2 Kolom FTI"),
]


def print_specification():
    print("=== STANDAR STRUKTUR BERKAS REPOSITORI GDLIB GUNADARMA ===")
    print("Setiap mahasiswa wajib memecah naskah final menjadi berkas PDF terpisah:")
    for code, desc in REQUIRED_GDLIB_FILES:
        print(f"  [{code:42}] : {desc}")
    print("==========================================================")


def audit_gdlib_folder(target_dir: Path) -> dict:
    existing_files = {f.name: f for f in target_dir.glob("*.pdf")}

    results = []
    missing_count = 0

    for code, desc in REQUIRED_GDLIB_FILES:
        # Penanganan kasus variasi nomor jika tidak ada lampiran (Bab I mulai dari 10)
        found = code in existing_files
        alt_found = False
        if not found:
            # Cari variasi umum (misal 18_JURNAL alih-alih 19_JURNAL)
            base_name = code.split("_", 1)[1] if "_" in code else code
            for ef in existing_files:
                if base_name in ef:
                    alt_found = True
                    found = True
                    break

        status = "SESUAI" if found else "TIDAK DITEMUKAN"
        if not found:
            missing_count += 1
        results.append({"code": code, "desc": desc, "status": status})

    return {
        "folder": str(target_dir),
        "total_expected": len(REQUIRED_GDLIB_FILES),
        "missing_count": missing_count,
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser(description="Validator Berkas Repositori GDLib Gunadarma")
    parser.add_argument("--dir", help="Path direktori berkas-berkas PDF skripsi")
    parser.add_argument("--spec", action="store_true", help="Tampilkan spesifikasi nama berkas baku GDLib")
    args = parser.parse_args()

    if args.spec or not args.dir:
        print_specification()
        if not args.dir:
            return

    target = Path(args.dir)
    if not target.is_dir():
        print(f"Error: direktori {target} tidak ditemukan.", file=sys.stderr)
        sys.exit(1)

    res = audit_gdlib_folder(target)
    print(f"\nAudit Folder: {target.name}")
    print(f"Total Berkas Diharapkan: {res['total_expected']}")
    print(f"Berkas Belum Ditemukan: {res['missing_count']}\n")

    for item in res["results"]:
        print(f"  [{item['status']:14}] {item['code']:42} ({item['desc']})")


if __name__ == "__main__":
    main()
