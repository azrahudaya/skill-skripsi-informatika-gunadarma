# Pedoman visual, diagram AI, gambar, dan metodologi evaluasi

Gunakan panduan ini saat membuat, mengaudit, atau merevisi ilustrasi sistem, diagram, visual berbasis data, serta skema metodologi pada Skripsi Informatika Gunadarma.

## 1. Standar diagram yang digenerate AI dan tool visual

Saat membuat diagram menggunakan AI (Midjourney, ChatGPT Canvas, DALL-E) atau tool berbasis kode (draw.io, Mermaid, Graphviz, PlantUML):

1. Larangan AI slop dan dekorasi non-akademik: dilarang gaya 3D glossy, gradien neon, bayangan berlebihan, atau karakter kartun generik; dilarang teks berbahasa asing acak/gibberish. Semua label memakai Bahasa Indonesia baku yang tajam dan terbaca. Bila memakai AI image generator, tambahkan prompt pembatas: `"clean academic technical diagram, draw.io style, flat design, white background, high-contrast monochrome/subtle grayscale, crisp legible typography, sharp vector outlines, Indonesian language labels"`.
2. Format dan resolusi: ekspor PNG resolusi tinggi (minimal 2400 piksel sisi panjang atau 300 DPI) atau vektor SVG; latar putih bersih (#FFFFFF), bukan transparan.
3. Keterbacaan fotokopi (grayscale safe): tetap terbaca saat difotokopi hitam putih; outline tegas (minimal 1.5 pt), teks sans-serif (Arial, Helvetica, Segoe UI) minimal 10 pt, arsiran atau label langsung untuk membedakan jalur/blok.

## 2. Katalog variasi diagram dalam Skripsi Informatika

Jangan mencampuradukkan diagram alur sistem dengan diagram metodologi penelitian.

### A. Diagram Metodologi Penelitian vs Diagram Alur Kerja Sistem

- **Diagram Alur Kerja Sistem (System Workflow)**: menggambarkan jalannya data dan logika komputasi dari masukan pengguna sampai keluaran (mis. validasi, pemrosesan, inferensi model, penyimpanan, keluaran). Memakai simbol baku flowchart (terminator oval, proses persegi, keputusan belah ketupat, I/O jajar genjang, basis data silinder).
- **Diagram Metodologi Penelitian (Research Methodology Flow)**: menggambarkan tahapan aktivitas peneliti dari awal sampai kesimpulan. Untuk Prototype: siklus iteratif (Planning, Modeling, Construction, Deployment, Communication) yang berputar bila sistem belum memadai, lalu bermuara ke evaluasi empiris. Untuk Waterfall/SDLC: tahapan linier bertingkat dari analisis kebutuhan sampai pengujian. Untuk CRISP-DM: enam tahap berurutan dengan kemungkinan kembali ke tahap sebelumnya.

### B. Pemodelan UML

- **Use Case Diagram**: batas sistem (system boundary) kotak yang membungkus use case elips; aktor di luar kotak (mis. pengguna di kiri, administrator di kanan); use case ringkas dan berorientasi fungsional bernilai (mis. `Mengirim Data`, `Melihat Riwayat`, `Mengelola Pengguna`). Dilarang membuat use case untuk aksi mekanis sepele (mis. `Mengetik Nama`, `Menekan Tombol`).
- **Activity Diagram**: langkah pemrosesan detail; swimlane vertikal memisahkan tanggung jawab (Pengguna, Antarmuka, Server/Backend); status awal (lingkaran solid), aktivitas (persegi berujung bulat), keputusan (belah ketupat), status akhir (lingkaran cincin).

### C. Storyboard dan Perancangan Antarmuka (Wireframe)

Digunakan untuk skenario percakapan atau alur navigasi aplikasi dari sudut pandang layar. Disusun multi-panel (mis. 4 panel horizontal atau 2x2) dengan judul panel dan nomor urut; setiap panel menampilkan tahapan interaksi kunci dan diberi caption resmi (mis. `Gambar 3.x Storyboard Antarmuka Aplikasi`).

### D. Struktur Navigasi Aplikasi

Bedakan empat arsitektur: linier (berurutan satu arah), non-linier (bebas), hierarki (pohon bercabang), dan campuran/komposit (kombinasi; paling umum pada aplikasi modern).

## 3. Standar grafik hasil evaluasi kuantitatif

1. Diagram batang: sumbu Y (kuantitas) mulai dari 0; beri nilai angka di atas setiap batang; pembedaan kategori memakai arsiran, bukan warna pelangi.
2. Histogram/distribusi frekuensi: tampilkan sebaran data empiris; cantumkan garis putus-putus untuk rata-rata (mean) dan median.
3. Grafik latensi/komposisi waktu (stacked bar/area): bedakan porsi waktu pemrosesan per komponen.

## 4. Struktur dan evaluasi Bab 3 sampai Bab 4

1. **Ruang Lingkup (Bab 1)**: memuat batasan kuantitatif terukur (format dan ukuran masukan, batas fungsional, lingkungan operasional, hak akses) bila relevan.
2. **Metode Penelitian (Bab 3)**: menjabarkan tahapan kerangka prosedur (CRISP-DM, SDLC/Waterfall, Prototype, Agile, SWDLC, Luther) secara kronologis dan prosedural, bukan hanya menyebut nama metodenya. Data, pra-pemrosesan, model, dan evaluasi terdokumentasi (lihat `references/bab3-metode.md`).
3. **Tinjauan Pustaka (Bab 2)**: definisikan istilah kunci pada judul; minimal 20 sumber (70% artikel ilmiah, 10 tahun terakhir).
4. **Hasil dan Pembahasan (Bab 4)**: sajikan temuan sesuai urutan tujuan, uji fungsional (black-box) dan uji kuantitatif (akurasi, F1, AUC, mAP, latensi), interpretasi kritis, kaitan dengan teori. Kode program pada lampiran berupa teks tercetak monospasi, bukan gambar screenshot.
