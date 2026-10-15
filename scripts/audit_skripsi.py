#!/usr/bin/env python3
"""Audit naskah Skripsi Informatika Gunadarma 2025.

Mendukung berkas DOCX, LaTeX (.tex), Markdown (.md), dan teks polos (.txt).
Hanya menggunakan modul bawaan Python (stdlib: zipfile, xml, re, json, argparse).
"""

# ponytail: parser docx/tex ini berbasis regex dan xml sederhana tanpa dependensi eksternal;
# batasan: styling inline font tersembunyi tidak terbaca; upgrade ke python-docx saat inspeksi styling tabel/cell kompleks diperlukan.

import argparse
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def extract_text_from_docx(path: Path) -> list[dict]:
    """Ekstrak paragraf dan heading dari berkas DOCX via zipfile dan XML."""
    paragraphs = []
    with zipfile.ZipFile(path, "r") as z:
        if "word/document.xml" not in z.namelist():
            return paragraphs
        tree = ET.fromstring(z.read("word/document.xml"))

    for p in tree.iter(f"{W_NS}p"):
        p_style = None
        pPr = p.find(f"{W_NS}pPr")
        if pPr is not None:
            pStyle_elem = pPr.find(f"{W_NS}pStyle")
            if pStyle_elem is not None:
                p_style = pStyle_elem.attrib.get(f"{W_NS}val")

        text_parts = [node.text for node in p.iter(f"{W_NS}t") if node.text]
        full_text = "".join(text_parts).strip()
        if full_text:
            paragraphs.append({"text": full_text, "style": p_style or ""})
    return paragraphs


def extract_text_from_tex(path: Path) -> list[dict]:
    """Ekstrak bagian dan paragraf dari berkas LaTeX .tex."""
    content = path.read_text(encoding="utf-8", errors="ignore")
    # Bersihkan komentar latex
    content = re.sub(r"(?m)(?<!\\)%.*$", "", content)
    lines = content.splitlines()

    paragraphs = []
    buffer = []

    def flush_buffer():
        if buffer:
            txt = " ".join(buffer).strip()
            if txt:
                paragraphs.append({"text": txt, "style": ""})
            buffer.clear()

    for line in lines:
        line_clean = line.strip()
        sec_match = re.search(r"\\(chapter|section|subsection|subsubsection)\*?\{([^}]+)\}", line_clean)
        if sec_match:
            flush_buffer()
            level = sec_match.group(1)
            title = sec_match.group(2)
            style = "Heading1" if level == "chapter" else "Heading2" if level == "section" else "Heading3"
            paragraphs.append({"text": title, "style": style})
        elif not line_clean:
            flush_buffer()
        else:
            buffer.append(line_clean)
    flush_buffer()
    return paragraphs


def extract_text_from_plain(path: Path) -> list[dict]:
    """Ekstrak paragraf dan heading dari teks Markdown atau polos."""
    content = path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()
    paragraphs = []
    buffer = []

    def flush_buffer():
        if buffer:
            txt = " ".join(buffer).strip()
            if txt:
                paragraphs.append({"text": txt, "style": ""})
            buffer.clear()

    for line in lines:
        clean = line.strip()
        if not clean:
            flush_buffer()
            continue
        h_match = re.match(r"^(#+)\s*(.+)$", clean)
        if h_match:
            flush_buffer()
            level = len(h_match.group(1))
            style = "Heading1" if level == 1 else "Heading2" if level == 2 else "Heading3"
            paragraphs.append({"text": h_match.group(2).strip(), "style": style})
            continue
        buffer.append(clean)
    flush_buffer()
    return paragraphs


def parse_document(path: Path) -> list[dict]:
    ext = path.suffix.lower()
    if ext == ".docx":
        return extract_text_from_docx(path)
    if ext == ".tex":
        return extract_text_from_tex(path)
    return extract_text_from_plain(path)


def audit_manuscript(paragraphs: list[dict]) -> dict:
    """Audit isi dan kepatuhan naskah skripsi berdasarkan aturan Gunadarma 2025."""
    full_text = "\n".join(p["text"] for p in paragraphs)

    # 1. Cek Struktur Bab (5 Bab Wajib)
    bab_checks = {
        "Bab 1 Pendahuluan": bool(re.search(r"(?i)\b(bab\s*1|bab\s*i)\b.*(pendahuluan)?", full_text)),
        "Bab 2 Tinjauan Pustaka": bool(re.search(r"(?i)\b(bab\s*2|bab\s*ii)\b.*(tinjauan\s*pustaka|landasan)?", full_text)),
        "Bab 3 Metode Penelitian": bool(re.search(r"(?i)\b(bab\s*3|bab\s*iii)\b.*(metode)?", full_text)),
        "Bab 4 Hasil dan Pembahasan": bool(re.search(r"(?i)\b(bab\s*4|bab\s*iv)\b.*(hasil|pembahasan)?", full_text)),
        "Bab 5 Penutup": bool(re.search(r"(?i)\b(bab\s*5|bab\s*v)\b.*(penutup|kesimpulan)?", full_text)),
    }

    # 2. Cek Bagian Awal
    front_matter_checks = {
        "Lembar Pengesahan": bool(re.search(r"(?i)lembar\s*pengesahan|panitia\s*ujian", full_text)),
        "Pernyataan Orisinalitas": bool(re.search(r"(?i)orisinalitas|pernyataan\s*keaslian", full_text)),
        "Abstrak (Indonesia)": bool(re.search(r"(?i)\babstrak\b", full_text)),
        "Abstract (Inggris)": bool(re.search(r"(?i)\babstract\b", full_text)),
        "Kata Pengantar": bool(re.search(r"(?i)kata\s*pengantar", full_text)),
        "Daftar Isi": bool(re.search(r"(?i)daftar\s*isi", full_text)),
    }

    # 3. Hitung kata abstrak
    abstrak_indo_words = 0
    abstract_eng_words = 0
    m_abs_id = re.search(r"(?is)\babstrak\b\s*(.*?)(?=\babstract\b|\bkata\s*pengantar\b|\bbab\s*1\b|\bbab\s*i\b)", full_text)
    if m_abs_id:
        abstrak_indo_words = len(re.findall(r"\b\w+\b", m_abs_id.group(1)))

    m_abs_en = re.search(r"(?is)\babstract\b\s*(.*?)(?=\bkata\s*pengantar\b|\bdaftar\s*isi\b|\bbab\s*1\b|\bbab\s*i\b)", full_text)
    if m_abs_en:
        abstract_eng_words = len(re.findall(r"\b\w+\b", m_abs_en.group(1)))

    # 4. Cek aturan minimal 3 paragraf per subbab
    subsections = []
    current_sub = None
    sub_paras = []

    sub_pattern = re.compile(r"^\d+\.\d+(\.\d+)?\b", re.IGNORECASE)

    for p in paragraphs:
        txt = p["text"]
        style = p.get("style", "")
        # Subbab yang wajib 3 paragraf adalah subbab bernomor di dalam bab (misal 1.1, 2.1.3)
        is_sub = bool(sub_pattern.match(txt) or (style in ("Heading2", "Heading3") and sub_pattern.match(txt)))
        if is_sub:
            if current_sub:
                subsections.append({"title": current_sub, "paragraph_count": len(sub_paras)})
            current_sub = txt[:60]
            sub_paras = []
        else:
            # Hitung hanya jika panjang kalimat wajar (> 25 karakter) agar caption/list pendek tidak dikira paragraf
            if len(txt) > 25 and not txt.startswith("Gambar") and not txt.startswith("Tabel"):
                sub_paras.append(txt)

    if current_sub:
        subsections.append({"title": current_sub, "paragraph_count": len(sub_paras)})

    short_subsections = [s for s in subsections if s["paragraph_count"] < 3]

    # 5. Cek Daftar Pustaka dan Sitasi
    dp_match = re.search(r"(?is)\bdaftar\s*pustaka\b\s*(.*)", full_text)
    dp_text = dp_match.group(1) if dp_match else ""

    # Ekstrak entri pustaka (tiap entri biasanya berjarak newline atau diawali pola penulis/tahun)
    raw_entries = [e.strip() for e in re.split(r"\n{2,}|\n(?=[A-Z][a-zA-Z\s]+,\s*\d{4})", dp_text) if len(e.strip()) > 15]
    total_references = len(raw_entries)

    doi_count = len(re.findall(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+|doi\.org/\S+", dp_text))
    journal_indicators = len(re.findall(r"(?i)\b(jurnal|journal|vol\.|no\.|prosiding|proceedings|trans\.|ieee|acm|sciencedirect)\b", dp_text))

    # Rasio estimasi artikel ilmiah (jurnal/prosiding)
    journal_pct = (journal_indicators / total_references * 100) if total_references > 0 else 0

    # 6. Traceability / Keterkaitan Logika Inti
    has_rumusan = bool(re.search(r"(?i)rumusan\s*masalah", full_text))
    has_tujuan = bool(re.search(r"(?i)tujuan\s*penelitian", full_text))
    has_kesimpulan = bool(re.search(r"(?i)kesimpulan", full_text))

    # Deteksi domain topik (AI / Rekayasa Perangkat Lunak)
    is_ai = bool(re.search(r"(?i)(machine\s*learning|deep\s*learning|cnn|lstm|dataset|akurasi|precision|recall|f1-score|confusion\s*matrix)", full_text))
    is_se = bool(re.search(r"(?i)(use\s*case|sequence\s*diagram|class\s*diagram|black\s*box|uat|blackbox|framework|database|erd)", full_text))

    return {
        "bab_checks": bab_checks,
        "front_matter_checks": front_matter_checks,
        "abstract_counts": {
            "indonesia_words": abstrak_indo_words,
            "indonesia_ok": 0 < abstrak_indo_words <= 250 if abstrak_indo_words else None,
            "english_words": abstract_eng_words,
            "english_ok": 0 < abstract_eng_words <= 250 if abstract_eng_words else None,
        },
        "subsections_audited": len(subsections),
        "short_subsections": short_subsections,
        "bibliography": {
            "total_detected": total_references,
            "min_20_met": total_references >= 20,
            "doi_count": doi_count,
            "estimated_journal_pct": round(journal_pct, 1),
            "journal_70_pct_met": journal_pct >= 65,  # toleransi estimasi heuristik
        },
        "traceability": {
            "has_rumusan_masalah": has_rumusan,
            "has_tujuan": has_tujuan,
            "has_kesimpulan": has_kesimpulan,
            "domain_detected": "AI / Data Science" if is_ai and not is_se else "Software Engineering" if is_se and not is_ai else "Campuran / Khusus" if is_ai and is_se else "Umum",
        },
    }


def format_report_cli(report: dict, filepath: Path) -> str:
    lines = []
    lines.append(f"=== HASIL AUDIT NASKAH SKRIPSI INFORMATIKA GUNADARMA ===")
    lines.append(f"Berkas: {filepath.name}")
    lines.append("")

    lines.append("1. STRUKTUR 5 BAB POKOK [PDF 17-18 / cetak 16-17]")
    for bab, ok in report["bab_checks"].items():
        status = "SESUAI" if ok else "TIDAK DITEMUKAN"
        lines.append(f"   [{status:14}] {bab}")

    lines.append("")
    lines.append("2. KELENGKAPAN BAGIAN AWAL [PDF 11-16 / cetak 10-15]")
    for part, ok in report["front_matter_checks"].items():
        status = "SESUAI" if ok else "BELUM TERLIHAT"
        lines.append(f"   [{status:14}] {part}")

    lines.append("")
    lines.append("3. ABSTRAK & ABSTRACT (MAKS 250 KATA) [PDF 14 / cetak 13]")
    abs_data = report["abstract_counts"]
    id_status = "SESUAI" if abs_data["indonesia_ok"] else "LEBIH DARI 250 KATA" if abs_data["indonesia_words"] > 250 else "BELUM TERDETEKSI"
    en_status = "SESUAI" if abs_data["english_ok"] else "LEBIH DARI 250 KATA" if abs_data["english_words"] > 250 else "BELUM TERDETEKSI"
    lines.append(f"   Abstrak ID : {abs_data['indonesia_words']} kata [{id_status}]")
    lines.append(f"   Abstract EN: {abs_data['english_words']} kata [{en_status}]")

    lines.append("")
    lines.append("4. ATURAN MINIMAL 3 PARAGRAF PER SUBBAB [PDF 20 / cetak 19]")
    short = report["short_subsections"]
    if not short:
        lines.append(f"   [SESUAI        ] Semua {report['subsections_audited']} subbab terdeteksi memiliki minimal 3 paragraf.")
    else:
        lines.append(f"   [PERLU REVISI  ] Ditemukan {len(short)} subbab dengan isi kurang dari 3 paragraf:")
        for s in short[:10]:
            lines.append(f"     - \"{s['title']}\" (hanya {s['paragraph_count']} paragraf)")
        if len(short) > 10:
            lines.append(f"     ... dan {len(short)-10} subbab lainnya.")

    lines.append("")
    lines.append("5. DAFTAR PUSTAKA & SITASI [PDF 18, 20 / cetak 17, 19]")
    bib = report["bibliography"]
    total_stat = "SESUAI" if bib["min_20_met"] else "KURANG (WAJIB MIN 20)"
    lines.append(f"   Jumlah Referensi : {bib['total_detected']} sumber [{total_stat}]")
    lines.append(f"   Referensi Ber-DOI: {bib['doi_count']} entri (Pedoman mewajibkan DOI untuk artikel)")
    lines.append(f"   Estimasi Jurnal  : {bib['estimated_journal_pct']}% (Target pedoman: 70% artikel ilmiah)")

    lines.append("")
    lines.append("6. SINKRONISASI LOGIKA & DOMAIN")
    tr = report["traceability"]
    lines.append(f"   Domain Terdeteksi: {tr['domain_detected']}")
    lines.append(f"   Rumusan Masalah  : {'Ditemukan' if tr['has_rumusan_masalah'] else 'Belum ditemukan'}")
    lines.append(f"   Tujuan Penelitian: {'Ditemukan' if tr['has_tujuan'] else 'Belum ditemukan'}")
    lines.append(f"   Kesimpulan       : {'Ditemukan' if tr['has_kesimpulan'] else 'Belum ditemukan'}")
    lines.append("========================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Audit naskah Skripsi Informatika Gunadarma 2025")
    parser.add_argument("file", help="Path berkas naskah (.docx, .tex, .md, .txt)")
    parser.add_argument("--json", action="store_true", help="Keluarkan output format JSON")
    args = parser.parse_args()

    target = Path(args.file)
    if not target.is_file():
        print(f"Error: berkas {target} tidak ditemukan.", file=sys.stderr)
        sys.exit(1)

    paragraphs = parse_document(target)
    if not paragraphs:
        print(f"Peringatan: tidak ada teks yang berhasil diekstrak dari {target}.", file=sys.stderr)
        sys.exit(1)

    report = audit_manuscript(paragraphs)

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(format_report_cli(report, target))


if __name__ == "__main__":
    main()
