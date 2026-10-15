# Panduan Pembuatan Skripsi Informatika dari Nol (Playbook AI dan Mahasiswa)

Panduan ini mengatur cara kerja AI agent saat mendampingi mahasiswa Informatika Universitas Gunadarma menyusun Skripsi dari tahap ide awal (nol) hingga naskah siap sidang dan revisi.

## Prinsip Interaksi AI saat Pembuatan dari Nol

1. **Jangan Melompat Bab**: AI tidak boleh langsung membuat Bab 4 (Hasil) jika Bab 1 (Masalah & Tujuan) dan Bab 3 (Metode) belum disepakati. Kerangka ilmiah wajib runtut.
2. **Jangan Mengarang Data Empiris**: AI membantu struktur kalimat, tinjauan teori, metodologi, dan kode pengujian; tetapi angka metrik evaluasi, sampel data riil, dan hasil uji lapangan harus bersumber dari eksperimen nyata mahasiswa.
3. **Patuhi Format Baku Sejak Draf Pertama**: Setiap subbab yang digenerate oleh AI wajib langsung memuat minimal tiga paragraf bermakna [PDF 20 / cetak 19], bukan poin-poin kosong.
4. **Bahasa Akademik Terse**: Gunakan Bahasa Indonesia formal deklaratif, hindari kata ganti orang pertama (saya/kami/penulis di tubuh kalimat), istilah asing dicetak miring, dan tanpa em dash.

---

## 9 Fase Eksekusi End-to-End

### Fase 0: Pemilihan Topik dan Formulasi Judul
- Bantu mahasiswa memilih track:
  * Track AI/Data Science (NLP, Computer Vision, Deep Learning, Prediksi Time-Series, Rekomendasi).
  * Track Rekayasa Sistem (Web terdistribusi, Mobile Flutter/React Native, IoT dengan MQTT/ESP32, Microservices).
- Rujuk 36 tema judul contoh Gunadarma di `references/contoh-dan-lampiran.md`.
- Formulasi Judul Standar Gunadarma [PDF 11 / cetak 10]:
  * Kalimat deklaratif, bermakna tunggal, tidak disingkat, tanpa tanda tanya.
  * Rumus: `[Metode / Algoritma yang Digunakan] + untuk + [Pemecahan Masalah / Fungsi] + pada + [Objek / Studi Kasus]`.
  * Contoh: "Penerapan Arsitektur Convolutional Neural Network untuk Klasifikasi Penyakit Daun Tomat pada Citra Tanaman Hortikultura".

### Fase 1: Penyusunan Proposal Skripsi
- Susun draf proposal:
  * Latar Belakang (masalah riil + data dukung + identifikasi gap dari 3 penelitian terdahulu).
  * Rumusan Masalah (pertanyaan fokus terukur).
  * Batasan Masalah (lingkup dataset/hardware/tools).
  * Tujuan Penelitian (simetris menjawab rumusan masalah).
  * Sistematika Penulisan (gambaran Bab 1 sampai Bab 5 secara naratif).
- Siapkan buku agenda bimbingan skripsi untuk disetujui dosen pembimbing.

### Fase 2: Eksperimen Teknis dan Rekayasa Kode
- Jika Track AI / Machine Learning:
  * Tentukan sumber dataset (Kaggle, UCI, atau data primer) dan verifikasi izin penggunaannya.
  * Buat skrip pra-pemrosesan: pastikan split train-val-test dilakukan sebelum scaling/normalisasi (cegah data leakage).
  * Bangun model baseline dan model yang diajukan.
  * Catat parameter pelatihan, seed acak, grafik loss/epoch, dan confusion matrix.
- Jika Track Rekayasa Sistem / Web / Mobile / IoT:
  * Buat diagram UML lengkap: Use Case, Activity, Sequence, dan Class Diagram.
  * Rancang skema database (ERD ternormalisasi 1NF-3NF dan DDL SQL).
  * Bangun implementasi program (backend API, frontend, koneksi sensor).
  * Rancang tabel skenario uji Blackbox dan skenario UAT/SUS.

### Fase 3: Penulisan Bab 1 sampai Bab 3
- Bab 1 Pendahuluan: Ikuti `references/bab1-pendahuluan.md`. Minimal 5 subbab, tiap subbab minimal 3 paragraf.
- Bab 2 Tinjauan Pustaka: Ikuti `references/bab2-tinjauan-pustaka.md`. Uraikan teori dasar algoritma, rumus matematis, dan tabel perbandingan penelitian terdahulu (`references/penelitian-terdahulu.md`).
- Bab 3 Metode Penelitian: Ikuti `references/bab3-metode.md`. Paparkan bagan alir riset, bahan dan alat, parameter uji, serta teknik evaluasi.

### Fase 4: Penulisan Bab 4 dan Bab 5
- Bab 4 Hasil dan Pembahasan: Ikuti `references/bab4-hasil-pembahasan.md`. Sajikan tabel hasil pengujian (caption di atas), grafik performa (caption di bawah), serta analisis mendalam mengenai korelasi hasil dengan teori di Bab 2.
- Bab 5 Penutup: Ikuti `references/bab5-penutup.md`. Tulis kesimpulan yang menjawab rumusan masalah secara lugas dengan data angka hasil riset, serta saran konstruktif yang aplikatif.

### Fase 5: Integrasi Sitasi dan Daftar Pustaka Harvard
- Kumpulkan minimal 20 referensi (minimal 14 artikel ilmiah/jurnal, maksimal 10 tahun terakhir).
- Pastikan setiap entri artikel ilmiah mencantumkan tautan DOI yang valid [PDF 20 / cetak 19].
- Gunakan format Harvard alfabetis sesuai panduan di `references/sitasi-dan-daftar-pustaka.md`.

### Fase 6: Penulisan Bagian Awal dan Abstrak
- Tulis Abstrak (Bahasa Indonesia) maksimal 250 kata dalam 1 paragraf, memuat masalah, tujuan, metode, hasil, dan simpulan.
- Tulis Abstract (Bahasa Inggris) maksimal 250 kata.
- Susun Halaman Judul, Lembar Pengesahan, Pernyataan Orisinalitas, Kata Pengantar, dan Daftar Isi otomatis (TOC).

### Fase 7: Audit Otomatis dan Cek Integritas
- Jalankan script auditor: `python3 scripts/audit_skripsi.py <naskah>`.
- Periksa keselarasan logika dengan matriks traceability di `references/audit-substansi-informatika.md`.
- Lakukan pengecekan similarity Turnitin (pastikan di bawah 20% sampai 25%).
- Masukkan deklarasi pemanfaatan AI generatif pada Kata Pengantar bila menggunakan AI dalam proses bantuan penulisan/coding.

### Fase 8: Pembuatan Luaran Wajib dan Persiapan Sidang
- Buat Artikel Ilmiah (2 kolom, 6-10 halaman) mengikuti `references/artikel-ilmiah-dan-manual-book.md`.
- Buat Manual Book sistem beranotasi langkah operasional.
- Siapkan slide presentasi sidang (12 slide) dan pelajari bank soal tanya-jawab di `references/alur-sidang-dan-revisi.md`.
- Setelah sidang selesai, susun tabel matriks perbaikan naskah pascasidang.
