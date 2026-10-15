# Panduan Penulisan Skripsi dengan LaTeX dan LyX

Pedoman Penulisan Skripsi Informatika Universitas Gunadarma 2025 secara eksplisit merekomendasikan penggunaan aplikasi text processing terstruktur seperti **LyX atau LaTeX** [PDF 21 / cetak 20]. Dokumen ini menyediakan template preamble dan pengaturan dokumen yang memenuhi standar Gunadarma.

## 1. Preamble Standar LaTeX (Gunadarma Informatika 2025)

Gunakan konfigurasi berikut pada dokumen utama (`main.tex`):

```latex
\documentclass[12pt,a4paper,oneside]{report}

% 1. Batas Margin: Atas 4 cm, Bawah 3 cm, Kiri 4 cm, Kanan 3 cm [PDF 19 / cetak 18]
\usepackage[top=4cm, bottom=3cm, left=4cm, right=3cm]{geometry}

% 2. Tipografi: Times New Roman 12 pt [PDF 19 / cetak 18]
\usepackage{newtxtext,newtxmath}

% 3. Pengaturan Spasi: 1.5 spasi untuk teks naskah [PDF 19 / cetak 18]
\usepackage{setspace}
\onehalfspacing

% 4. Bahasa dan Karakter Khusus
\usepackage[indonesian]{babel}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}

% 5. Format Caption Gambar dan Tabel [PDF 20 / cetak 19]
% Judul tabel di atas tengah, judul gambar di bawah tengah
\captionsetup[table]{position=top, justification=centering, labelsep=period}
\captionsetup[figure]{position=bottom, justification=centering, labelsep=period}

% 6. Penataan Header dan Footer (Penomoran Halaman) [PDF 20 / cetak 19]
\usepackage{fancyhdr}
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyfoot[C]{\thepage} % Awal bab: nomor di tengah bawah
  \renewcommand{\headrulewidth}{0pt}
}
\fancypagestyle{maincontent}{
  \fancyhf{}
  \fancyhead[R]{\thepage} % Halaman isi lanjutan: kanan atas
  \renewcommand{\headrulewidth}{0pt}
}

% 7. Kode Program: Courier/Monospace 8 pt, Spasi Tunggal [PDF 18 / cetak 17]
\usepackage{listings}
\lstset{
  basicstyle=\fontsize{8}{10}\ttfamily,
  breaklines=true,
  numbers=left,
  numberstyle=\tiny,
  frame=single,
  showstringspaces=false
}

% 8. Daftar Pustaka Harvard + Wajib DOI [PDF 20 / cetak 19]
\usepackage[backend=biber,style=authoryear,sorting=nyt,maxcitenames=2]{biblatex}
\usepackage{url}
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=blue
}
\addbibresource{daftar-pustaka.bib}
```

## 2. Struktur Dokumen Utama (`main.tex`)

```latex
\begin{document}

% ---------------- BAGIAN AWAL (Nomor Romawi Kecil di Tengah Bawah) ----------------
\pagestyle{plain}
\pagenumbering{roman}

% Halaman Judul (Nomor dihitung tapi tidak ditampilkan)
\input{frontmatter/judul}
\newpage

% Lembar Pengesahan (Nomor dihitung tapi tidak ditampilkan)
\input{frontmatter/pengesahan}
\newpage

% Pernyataan Orisinalitas
\input{frontmatter/orisinalitas}
\newpage

% Abstrak Indonesia (Spasi Tunggal, Maks 250 Kata)
\begin{singlespace}
\input{frontmatter/abstrak}
\end{singlespace}
\newpage

% Abstract English (Single Space, Max 250 Words)
\begin{singlespace}
\input{frontmatter/abstract_en}
\end{singlespace}
\newpage

% Kata Pengantar
\input{frontmatter/pengantar}
\newpage

% Daftar Isi, Gambar, dan Tabel
\tableofcontents
\newpage
\listoffigures
\newpage
\listoftables
\newpage

% ---------------- BAGIAN ISI (Nomor Arab, 1.5 Spasi) ----------------
\cleardoublepage
\pagenumbering{arabic}
\pagestyle{maincontent}

% Bab 1 sampai Bab 5
\input{chapters/bab1-pendahuluan}
\input{chapters/bab2-tinjauan-pustaka}
\input{chapters/bab3-metode}
\input{chapters/bab4-hasil-pembahasan}
\input{chapters/bab5-penutup}

% ---------------- BAGIAN AKHIR (Daftar Pustaka & Lampiran) ----------------
\printbibliography[title={DAFTAR PUSTAKA}]
\newpage

% Lampiran (Penomoran L-1, L-2, ...) [PDF 18 / cetak 17]
\appendix
\renewcommand{\thepage}{L-\arabic{page}}
\setcounter{page}{1}
\input{appendices/lampiran-kode}

\end{document}
```

## 3. Format Entri BibTeX (`daftar-pustaka.bib`)

Pastikan setiap entri artikel ilmiah memiliki field `doi` aktif:

```bibtex
@article{sari2022penerapan,
  author  = {Sari, R. and Jannah, M. and Meuraxa, A. and Syahfitri, D. and Omar, K.},
  title   = {Penerapan Deep Learning untuk Deteksi Citra Medis},
  journal = {Jurnal Teknologi Sistem Informasi},
  year    = {2022},
  volume  = {14},
  number  = {2},
  pages   = {112--120},
  doi     = {10.35957/jtsi.v14i2.2891}
}

@book{pressman2020software,
  author    = {Pressman, Roger S. and Maxim, Bruce R.},
  title     = {Software Engineering: A Practitioner's Approach},
  edition   = {9th},
  publisher = {McGraw-Hill Education},
  address   = {New York},
  year      = {2020}
}
```

## 4. Pengaturan Naskah di LyX

Bila menggunakan antarmuka grafis LyX:
1. **Document Class**: Buka `Document` -> `Settings...` -> `Document Class`. Pilih `Report`.
2. **Page Layout**: Pada `Page Margins`, hilangkan centang `Default margins`. Isi Top: 4 cm, Bottom: 3 cm, Left: 4 cm, Right: 3 cm.
3. **Fonts**: Pilih `Times New Roman` untuk Roman, `Courier` untuk Monospace. Base size: `12`.
4. **Text Layout**: Line spacing pilih `Onehalf`. Indentation: uncheck `Indent paragraph` bila menggunakan pemisah paragraf berjarak.
5. **PDF Properties**: Aktifkan Hyperlinks (hyperref), pilih text color hitam untuk cetak formal.
6. **Bibliography**: Gunakan BibTeX atau Biber dengan style `authoryear`.
