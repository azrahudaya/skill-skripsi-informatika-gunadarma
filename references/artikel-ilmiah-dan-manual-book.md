# Panduan Artikel Ilmiah dan Manual Book Skripsi

Kewajiban luaran skripsi Program Studi Informatika FTI Universitas Gunadarma mencakup dua produk utama di samping naskah skripsi: **Artikel Ilmiah** dan **Manual Book** [PDF 22 / cetak 21].

## 1. Artikel Ilmiah (Scientific Article)

Artikel ilmiah merupakan naskah ringkas hasil penelitian skripsi yang ditujukan untuk publikasi ilmiah atau prosiding seminar/jurnal.

### Ketentuan Format Umum
- Jumlah Halaman: Umumnya 6 sampai 10 halaman (format 2 kolom simetris, kecuali Judul, Penulis, dan Abstrak yang dibuat 1 kolom).
- Ukuran Kertas: A4, margin standar (atas 2.5 cm, bawah 2.5 cm, kiri 2.5 cm, kanan 2.5 cm atau mengikuti template prodi).
- Font: Times New Roman 10 pt (isi teks), spasi tunggal (single spacing).
- Penulis: Nama mahasiswa diikuti nama dosen pembimbing (tanpa gelar akademik), alamat email resmi/kampus, dan afiliasi (Program Studi Informatika, Fakultas Teknologi Industri, Universitas Gunadarma).

### Struktur Isi Artikel Ilmiah
1. **Judul**: Maksimal 15 kata, jelas, menggambarkan masalah dan solusi. Kapital awal kata atau uppercase sesuai template.
2. **Abstrak & Kata Kunci**: Bahasa Indonesia dan Bahasa Inggris, 150-200 kata, 1 paragraf, memuat latar belakang singkat, tujuan, metode, hasil utama, dan simpulan. Kata kunci 3-5 istilah.
3. **I. Pendahuluan**:
   - Latar belakang masalah dan urgensi penelitian.
   - Tinjauan literatur singkat (gap riset dari 3-5 penelitian relevan).
   - Tujuan penelitian dan kontribusi ilmiah.
4. **II. Metode Penelitian**:
   - Data penelitian (sumber data, jumlah, pra-pemrosesan).
   - Kerangka metode atau arsitektur sistem yang diajukan.
   - Skenario pengujian dan metrik evaluasi yang digunakan.
5. **III. Hasil dan Pembahasan**:
   - Paparan data hasil pengujian dalam bentuk tabel dan grafik ringkas.
   - Analisis mendalam mengenai temuan penelitian.
   - Perbandingan performa dengan metode pembanding atau baseline.
6. **IV. Kesimpulan**:
   - Jawaban singkat atas tujuan penelitian berdasarkan hasil pengujian.
   - Keterbatasan dan saran pengembangan selanjutnya.
7. **Daftar Pustaka**:
   - Format Harvard, minimal 10-15 referensi terpenting dari naskah skripsi.
   - Wajib mencantumkan DOI artikel jurnal.

---

## 2. Manual Book (Petunjuk Penggunaan Sistem)

Manual book wajib dibuat untuk skripsi yang menghasilkan produk rekayasa perangkat lunak, aplikasi cerdas, model inferensi, atau perangkat IoT.

### Struktur Manual Book
1. **Halaman Sampul**:
   - Judul Aplikasi/Sistem dan nomor versi (misal v1.0.0).
   - Nama Penulis, NPM, Program Studi Informatika Gunadarma.
   - Tangkapan layar antarmuka utama sebagai cover visual.
2. **Deskripsi Umum Sistem**:
   - Penjelasan singkat fungsi sistem, target pengguna, dan manfaat operasional.
3. **Kebutuhan Sistem Minimum (System Requirements)**:
   - Hardware: Spesifikasi minimum CPU, RAM, GPU (bila menggunakan deep learning), kapasitas penyimpanan, dan kamera/sensor.
   - Software: Sistem operasi (Windows/Linux/macOS/Android), runtime environment (Python 3.x, Node.js, JVM), framework, library dependensi, serta versi database.
4. **Petunjuk Instalasi dan Konfigurasi Lingkungan**:
   - Langkah clone repositori / ekstrak berkas arsip.
   - Konfigurasi environment variables (.env, koneksi database, API key).
   - Perintah instalasi dependensi (misal `pip install -r requirements.txt` atau `npm install`).
   - Perintah migrasi basis data dan seeding data awal.
   - Perintah menjalankan server/aplikasi (lokal maupun container Docker).
5. **Panduan Pengoperasian Fitur per Aktor**:
   - Alur Login, Hak Akses, dan Pengaturan Profil.
   - Modul Utama 1: Input data, preprocessing, atau transaksi (sertakan tangkapan layar antarmuka beranotasi nomor langkah).
   - Modul Utama 2: Proses komputasi, training/inferensi model, atau pemrosesan logika bisnis.
   - Modul Utama 3: Output laporan, visualisasi grafik, atau ekspor data.
6. **Penanganan Masalah (Troubleshooting & FAQ)**:
   - Daftar kemungkinan pesan error dan solusi penanganannya.
   - Catatan batasan sistem dan kontak pengembang.
