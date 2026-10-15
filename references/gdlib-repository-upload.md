# Pola Berkas dan Standar Unggah Repository Perpustakaan Gunadarma (GDLib)

Berdasarkan analisis empiris 52 berkas skripsi resmi lulusan Informatika Universitas Gunadarma di repositori digital (GDLib), seluruh naskah akhir wajib dipecah (*split*) menjadi berkas-berkas PDF terpisah dengan konvensi penamaan bernomor baku sebelum diserahkan ke perpustakaan.

---

## 1. Konvensi Penamaan Berkas PDF Perpustakaan (01 sampai 19)

Setiap mahasiswa wajib menyiapkan satu folder terkompresi atau berkas terpisah dengan format nama persis sebagai berikut:

| Nomor Berkas | Nama File Baku GDLib | Isi Dokumen | Catatan Format Khusus |
|---|---|---|---|
| 01 | `01_COVER_PENULISAN.pdf` | Sampul luar dan halaman judul naskah | Nomor halaman `i` (dihitung, tidak dicetak) |
| 02 | `02_PERNYATAAN_ORIGINALITAS_PUBLIKASI.pdf` | Lembar pernyataan orisinalitas bermeterai | Menampilkan nomor halaman `ii` di tengah bawah |
| 03 | `03_PARAF_STEMPEL_LEMBAR_PENGESAHAN.pdf` | Lembar pengesahan hasil scan fisik resmi | Wajib memuat tanda tangan pembimbing, penguji, dan stempel basah BAAK |
| 04 | `04_ABSTRAKSI_BAHASA_INDONESIA.pdf` | Abstrak Bahasa Indonesia | 1 paragraf, maks 250 kata, ada rentang tahun pustaka di bawah |
| 05 | `05_ABSTRAKSI_BAHASA_INGGRIS.pdf` | Abstract Bahasa Inggris | 1 paragraf, maks 250 kata, ada rentang tahun bibliography |
| 06 | `06_KATA_PENGANTAR.pdf` | Kata Pengantar | Memuat 7 hierarki ucapan terima kasih resmi Gunadarma |
| 07 | `07_DAFTAR_ISI.pdf` | Daftar Isi | Dihasilkan dari Table of Contents (TOC) otomatis |
| 08 | `08_DAFTAR_TABEL.pdf` | Daftar Tabel | Berisi nomor tabel per bab dan halaman |
| 09 | `09_DAFTAR_GAMBAR.pdf` | Daftar Gambar | Berisi nomor gambar per bab dan halaman |
| 10 | `10_DAFTAR_LAMPIRAN.pdf` | Daftar Lampiran | Penomoran halaman lampiran `L-x` (jika ada lampiran) |
| 11 | `11_BAB_I.pdf` | Bab 1 Pendahuluan | Halaman awal bab nomor 1 di tengah bawah, halaman isi kanan atas |
| 12 | `12_BAB_II.pdf` | Bab 2 Tinjauan Pustaka | Landasan teori dan tabel penelitian terdahulu |
| 13 | `13_BAB_III.pdf` | Bab 3 Metode Penelitian | Bagan alir, data, dan perancangan sistem/model |
| 14 | `14_BAB_IV.pdf` | Bab 4 Hasil dan Pembahasan | Data kuantitatif pengujian dan analisis mendalam |
| 15 | `15_BAB_V.pdf` | Bab 5 Penutup | Kesimpulan (menjawab rumusan masalah) dan Saran |
| 16 | `16_DAFTAR_PUSTAKA.pdf` | Daftar Pustaka | Format Harvard, minimal 20 sumber, wajib DOI aktif |
| 17 | `17_LAMPIRAN.pdf` | Lampiran Naskah | Kode sumber (8 pt single space), tabel data, atau hasil uji |
| 18 | `18_MANUAL_BOOK.pdf` | Petunjuk Operasional Sistem | Khusus skripsi yang menghasilkan aplikasi/sistem/model |
| 19 | `19_JURNAL.pdf` | Artikel Ilmiah Publikasi | Format 2 kolom FTI (6-10 halaman) dengan nama pembimbing |

*Catatan*: Jika skripsi tidak memiliki lampiran terpisah, penomoran Bab 1 dapat dimulai dari `10_BAB_I.pdf` dan file jurnal menjadi `18_JURNAL.pdf`. Pola paling umum di FTI Gunadarma adalah 19 file lengkap.

---

## 2. Pola Penulisan Artikel Ilmiah Resmi (`19_JURNAL.pdf`)

Dari analisis berkas riil di GDLib, artikel ilmiah luaran skripsi Informatika Gunadarma memiliki pola standar:
1. **Judul Artikel**: Ditulis Title Case atau Uppercase, simetris tengah.
2. **Penulis dan Afiliasi**:
   - Penulis 1: Nama Mahasiswa (disertai NPM di bawah nama atau di samping).
   - Penulis 2: Nama Dosen Pembimbing (tanpa gelar atau dengan gelar sesuai template jurnal).
   - Afiliasi: Jurusan Informatika, Fakultas Teknologi Industri, Universitas Gunadarma.
   - Email: Email mahasiswa dan email resmi dosen pembimbing (`@staff.gunadarma.ac.id`).
3. **Format Layout**:
   - Judul, Penulis, dan Abstrak dibuat 1 kolom selebar halaman.
   - Isi teks (Pendahuluan, Metode, Hasil dan Pembahasan, Kesimpulan, Daftar Pustaka) dibuat 2 kolom simetris.
   - Menggunakan font Times New Roman 10 pt dengan spasi tunggal (single spacing).

---

## 3. Pola Data Empiris Pejabat Resmi Gunadarma di Kata Pengantar

Berdasarkan berkas naskah 2025/2026 di GDLib, urutan dan nama pejabat yang tertera adalah:
1. `Prof. Dr. E. S. Margianti, S.E., M.M.` (selaku Rektor Universitas Gunadarma).
2. `Prof. Dr. Ing. Adang Suhendra, S.Si., S.Kom., M.Sc.` (selaku Dekan Fakultas Teknologi Industri).
3. `Prof. Dr. Lintang Yuniar Banowosari, S.Kom., M.Sc.` (selaku Ketua Program Studi Informatika).
4. `Dr. Edi Sukirman, S.Si., MM., M.I.Kom.` (selaku Kepala Bagian Sidang Ujian).
5. Nama Dosen Pembimbing (sesuai SK pembimbing di Studentsite).
6. Orang Tua dan Keluarga.
7. Rekan-rekan mahasiswa seangkatan.

---

## 4. Distribusi Topik Skripsi Informatika Gunadarma Riil

Dari 52 sampel skripsi terkini di GDLib:
- **Kecerdasan Buatan / Data Science (46.2%)**:
  Didominasi Computer Vision (YOLOv11, EfficientNetV2, MobileNetV2, ResNet-50, MediaPipe), NLP (Transformer, BERT, S-BERT, TF-IDF Cosine Similarity), dan Deep Learning medis/pertanian. Metodologi paling banyak dipakai adalah CRISP-DM.
- **Rekayasa Perangkat Lunak / Web / Mobile (44.2%)**:
  Didominasi aplikasi berbasis Streamlit (untuk inferensi model AI), Flutter (mobile calisthenics/pose detection), dan Web Full-Stack (sistem inventory, SPK metode AHP/SAW, sistem rekomendasi). Metodologi paling banyak adalah SDLC Waterfall dan Agile.
- **Pengembangan Game Komputasi (9.6%)**:
  Didominasi Godot Engine dan Unity (2D/3D platformer dengan FSM AI untuk NPC dan algoritma pathfinding A*).
