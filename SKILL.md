---
name: skill-skripsi-informatika-gunadarma
description: Use when writing or auditing Gunadarma Informatika Skripsi. Panduan, kerangka, dan audit naskah Skripsi Prodi Informatika Universitas Gunadarma berbasis Buku Pedoman Penulisan Skripsi 2025.
version: 1.0.0
author: Azra Hudaya, Hermes Agent
license: Proprietary
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Gunadarma, Informatika, Skripsi, penulisan-ilmiah, pedoman-2025]
    category: productivity
---
# Pedoman Penulisan Skripsi Informatika Gunadarma 2025

Acuan utama: Buku Pedoman Penulisan Skripsi 2025, Program Studi Informatika, Fakultas Teknologi Industri, Universitas Gunadarma, PDF 34 halaman. Rujukan ditulis `PDF n / cetak m`; halaman PDF 1 adalah sampul tanpa teks, halaman PDF 2 sampai 34 berangka cetak 1 sampai 33. Gunakan pedoman asli yang diberikan pengguna untuk memeriksa ulang kutipan dan aturan bila ada edisi lebih baru. `references/cakupan-halaman.md` memetakan seluruh 34 halaman sumber ke bagian skill ini. `references/contoh-dan-lampiran.md` menginventarisasi 36 tema judul dan Lampiran 6.1 sampai 6.9. `references/konflik-visual-lampiran.md` merinci tata letak contoh dan ketidaksesuaian ukuran yang tidak terlihat dari ekstraksi teks. Untuk redaksi, tampilan, logo, dan detail yang perlu dibaca persis, buka PDF pedoman asli. Salinan atau transkripsi lengkap PDF tidak disertakan dalam distribusi publik skill ini.

Skill ini **khusus Skripsi**, bukan Penulisan Ilmiah (PI). Skripsi adalah karya ilmiah akhir jalur Tugas Akhir semester 8 untuk gelar Sarjana Informatika (S1), dengan cakupan riset dan kontribusi ilmiah yang lebih mendalam daripada PI [PDF 4 / cetak 3]. Untuk PI, gunakan skill pedoman PI, bukan skill ini.

## Kapan dipakai

- Memilih topik, menyusun proposal, membuat atau mengaudit Skripsi Informatika Gunadarma berdasarkan pedoman 2025.
- Menulis atau memperbaiki halaman judul, bagian awal, lima bab isi, daftar pustaka, lampiran, artikel ilmiah, dan manual book.
- Menjawab pertanyaan tentang format, isi, sitasi, etika penulisan, bimbingan, atau pengumpulan naskah.
- Untuk revisi DOCX pascasidang, baca dokumen Word berurutan termasuk tabel; periksa font, paragraf, header tabel, penomoran halaman, lalu render ke PDF dan cek halaman yang berubah. Skill ini tidak mewajibkan skill eksternal tertentu.

Jangan terapkan otomatis ke PI, prodi lain, atau edisi pedoman lain. Jangan anggap contoh judul, angka halaman, nama pejabat, dan teks contoh sebagai persyaratan universal. Bedakan `WAJIB`, `SARAN`, `CONTOH`, dan `AMBIGU`; bila pembimbing atau administrasi memberi ketentuan terkini yang berbeda, minta bukti resmi, catat perbedaan, dan jangan diam-diam menimpa isi pedoman.

**Di luar cakupan buku pedoman tertulis 2025:** prosedur resmi pendaftaran sidang, busana sidang, berkas sidang BAAK, dan revisi pascasidang sengaja tidak dirinci di dalam buku pedoman PDF 2025 [PDF 22 / cetak 21] melainkan diatur melalui portal resmi BAAK dan Prodi. Namun untuk menjawab kebutuhan menyeluruh mahasiswa, skill ini melengkapinya dengan panduan operasional praktis, slide presentasi, simulasi tanya-jawab, dan matriks revisi di `references/alur-sidang-dan-revisi.md`.

## Alur kerja

Untuk membuat naskah dari nol, ikuti 9 fase eksekusi di `references/panduan-pembuatan-dari-nol.md`. Untuk audit naskah, jalankan tool otomatis `python3 scripts/audit_skripsi.py <naskah>` dan ikuti alur audit di `references/alur-audit.md`. Untuk audit substansi teknis AI/Data Science, Rekayasa Perangkat Lunak, dan penelusuran benang merah logika (traceability), baca `references/audit-substansi-informatika.md`. Untuk membuat draf naskah lengkap, baca `references/draf-dokumen.md` serta `references/panduan-latex-lyx.md` (untuk LaTeX/LyX). Untuk luaran wajib berupa artikel ilmiah dan petunjuk sistem, baca `references/artikel-ilmiah-dan-manual-book.md`. Untuk bab isi, baca referensi bab yang sesuai: `references/bab1-pendahuluan.md` sampai `references/bab5-penutup.md`. Untuk visual dan lampiran kode, baca `references/visual-dan-lampiran-kode.md` dan `references/pedoman-visual-dan-evaluasi.md`. Untuk sitasi dan daftar pustaka, baca `references/sitasi-dan-daftar-pustaka.md`. Untuk sidang dan pascasidang, baca `references/alur-sidang-dan-revisi.md`.

1. Temukan PDF pedoman dan naskah Skripsi versi terakhir. Pastikan dokumen benar-benar edisi Prodi Informatika 2025. Rujuk halaman PDF dan angka tercetak agar lokasi aturan bisa diverifikasi. Untuk audit format visual, baca `references/konflik-visual-lampiran.md` sebelum menilai contoh sebagai patokan.
2. Tentukan jenis tugas: perencanaan topik/proposal, penulisan, audit, atau pengumpulan. Untuk audit, buat matriks `aturan | status | bukti lokasi dokumen | halaman pedoman | tindakan` dan periksa semua butir relevan di bawah. Jangan mengklaim kelulusan hanya dari pencarian kata; cek isi, tata letak, nomor halaman, dan berkas akhir.
3. Pisahkan aturan eksplisit dari contoh. Isi variabel (identitas, tanda tangan, foto, tanggal sidang/lulus, pejabat, referensi, hasil uji, jumlah halaman, tautan program) hanya dari data nyata. Jangan membuat hasil penelitian, pustaka, tanda tangan, atau fakta administratif palsu.
4. Jika pedoman bertentangan, catat kedua halaman di `references/ketidakselarasan.md`, gunakan contoh lampiran untuk membaca maksud tanpa menyulapnya menjadi aturan, dan konfirmasi kepada pembimbing/prodi bila berdampak pada penerimaan naskah.
5. Validasi akhir: hitung referensi dan artikel ilmiah, cocokkan sitasi bolak-balik, periksa format setiap bagian, hitung halaman pokok, uji berkas sumber dan PDF akhir, lalu cek persyaratan administratif terkini pada kanal resmi sebelum pengiriman.

## 1. Ruang lingkup, tujuan, dan bentuk Skripsi [PDF 4-7 / cetak 3-6]

- Pengertian: mahasiswa Program Studi Informatika wajib menyusun karya tulis ilmiah. PI menjadi syarat gelar setara sarjana muda pada semester enam; Skripsi disusun mahasiswa jalur Tugas Akhir berupa Skripsi pada semester delapan untuk memperoleh gelar Sarjana Informatika, dengan cakupan riset lebih mendalam dan kontribusi ilmiah lebih signifikan [PDF 4 / cetak 3].
- Lima tujuan penyusunan Skripsi: (1) menerapkan pengetahuan dan keterampilan akademik; (2) melatih kemampuan penelitian; (3) mengembangkan pola pikir kritis, logis, dan kreatif; (4) meningkatkan kemampuan komunikasi ilmiah; (5) memberikan kontribusi ilmiah [PDF 4-5 / cetak 3-4].
- Dua bentuk Skripsi [PDF 4 / cetak 3]:
  - *Berbasis penelitian*: memuat objek yang diteliti, permasalahan yang hendak dipecahkan, hipotesis yang diuji, metode, hasil, dan potensi pengembangan.
  - *Berbentuk rancangan*: memuat objek yang dirancang, masalah yang diselesaikan, ide rancangan, metode perancangan, hasil rancangan, serta kelebihan dan kelemahannya.
- 36 tema judul contoh (NLP, computer vision, machine learning, big data, smart city, IoT, dan seterusnya) dicatat lengkap di `references/contoh-dan-lampiran.md`. Semua judul contoh hanya ilustrasi, bukan topik yang diwajibkan [PDF 5-7 / cetak 4-6].
- Ketentuan judul: ringkas dan jelas; kalimat deklaratif, bukan kalimat tanya; tegas, bermakna tunggal, tidak mengulang kata, bukan singkatan; menggambarkan permasalahan, metode, dan objek; kata asing dicetak miring [PDF 11 / cetak 10].

## 2. Struktur naskah dan bagian awal [PDF 11-16 / cetak 10-15]

Tiga bagian: Bagian Awal, Bagian Isi, Bagian Akhir. Urutan bagian awal: (a) Halaman Judul, (b) Lembar Pengesahan, (c) Pernyataan Orisinalitas dan Publikasi, (d) Abstrak, (e) Abstract, (f) Kata Pengantar, (g) Daftar Isi, (h) Daftar Tabel / Daftar Gambar / Daftar Lampiran [PDF 11 / cetak 10]. Panduan detail dan redaksi baku setiap halaman diatur di `references/bagian-awal-naskah.md`.

- **Halaman Judul**: memuat Nama Universitas, Nama Fakultas, Logo, Judul, Nama Penulis, NPM, Program Studi, Nama Pembimbing, Tujuan dan dalam rangka apa karya dibuat, Kota, Tahun Pembuatan Skripsi [PDF 11 / cetak 10]. Diketik simetris tengah, Times New Roman, spasi tunggal; logo Gunadarma diameter 6 cm; Nama Universitas, Nama Fakultas, Judul, Kota, dan Tahun 14 pt kapital; Nama Penulis, NPM, Program Studi, Pembimbing, Tujuan, dan dalam rangka apa dibuat 12 pt. Contoh Lampiran 6.1 memakai redaksi `Disusun Oleh :` dan mencantumkan `Diajukan Guna Melengkapi Sebagian Syarat Dalam Mencapai Gelar Sarjana Strata Satu (S1)`. Lihat `references/konflik-visual-lampiran.md` untuk perbedaan ukuran pada contoh.
- **Pernyataan Orisinalitas dan Publikasi**: memuat Nama, NPM, Judul Skripsi, Tanggal Sidang, Tanggal Lulus, dan pernyataan karya sendiri serta izin publikasi penuh oleh Universitas. TNR 12 pt, spasi 1,5, rata kiri-kanan [PDF 11 / cetak 10]. Lampiran 6.2 menampilkan redaksi lengkap dan penutup `Jakarta, tanggal`, tanda tangan, nama penulis. Jangan isi tanggal atau tanda tangan sebelum faktanya tersedia.
- **Lembar Pengesahan**: memuat Judul Skripsi, Nama Mahasiswa, NPM, Tanggal Lulus, dan **tabel Panitia Ujian** berisi Ketua Sidang, Sekretaris Sidang, Pembimbing, dan Penguji [PDF 12 / cetak 11]. Tabel tiga kolom: No Urut, Nama, Kedudukan. Ditandatangani Pembimbing dan Kepala Bagian Sidang Ujian; bila dua pembimbing, ditandatangani Pembimbing 1, Pembimbing 2, dan Kepala Bagian Sidang. Nama pembimbing harus satu baris. TNR 12 pt, spasi 1. Template mengacu https://baak.gunadarma.ac.id/sidang/front/page_detail/2/DokumenSidang . Cek nama pejabat saat finalisasi.
- **Abstrak**: ikhtisar memuat permasalahan, tujuan, metode, hasil, dan kesimpulan. Maksimum 250 kata, satu paragraf, TNR 12 pt, spasi tunggal [PDF 14 / cetak 13]. Nama Mahasiswa, NPM, Judul, Program Studi, dan kata kunci ditulis di atas abstrak; kata kunci 3 sampai 5 dalam bahasa abstrak masing-masing. Di bawah abstrak ditulis tahun Daftar Pustaka yang digunakan. Istilah asing kecuali nama dicetak miring. Lampiran 6.4 menampilkan baris `Skripsi. Program Studi Informatika, Fakultas Teknologi Industri, Universitas Gunadarma, tahun` dan ringkasan jumlah halaman `(+ xiv + 92 + Lampiran)` sebagai CONTOH; hitung ulang setelah naskah final.
- **Abstract**: versi Bahasa Inggris dari abstrak, maksimum 250 kata, halaman terpisah [PDF 14 / cetak 13]. Lampiran 6.5.
- **Kata Pengantar**: ucapan terima kasih; nama pihak yang dibantu dicantumkan gelar akademik dan sebaiknya rincikan bantuannya. TNR 12 pt, spasi 1,5 (before/after 0); judul 14 pt tebal kapital; jarak judul ke isi 2 x 1,5 spasi [PDF 14-15 / cetak 13-14]. Urutan pihak: (1) Rektor, (2) Dekan, (3) Ketua Program Studi, (4) Kepala Bagian Sidang Ujian, (5) Dosen Pembimbing (bila dua, no. 5 Pembimbing 1 dan no. 6 Pembimbing 2), (6) Orang Tua dan Keluarga, (7) Teman-teman. Template mengacu https://baak.gunadarma.ac.id/sidang/front/page_detail/2/DokumenSidang . Lampiran 6.6.
- **Daftar Isi**: memuat semua bagian dan nomor halaman, ditulis sama dengan isi. TNR 12 pt spasi tunggal; judul tiap bab 14 pt tebal kapital; jarak judul ke isi 3 spasi; subbab maksimum 3 level; **dibuat otomatis dengan Table of Contents (TOC)** [PDF 15 / cetak 14]. Lampiran 6.7.
- **Daftar Tabel / Daftar Gambar / Daftar Lampiran**: TNR 12 pt spasi tunggal; judul daftar 14 pt tebal kapital [PDF 16 / cetak 15]. Daftar Tabel memuat semua tabel dengan nomor, judul, dan halaman; Daftar Gambar memuat gambar, grafik, diagram, ilustrasi; Daftar Lampiran memuat dokumen pendukung dengan penomoran urut. Lampiran 6.8.

## 3. Lima bab isi dan bagian akhir [PDF 17-18 / cetak 16-17]

Bagian isi: (1) Pendahuluan, (2) Tinjauan Pustaka, (3) Metode Penelitian, (4) Hasil dan Pembahasan, (5) Penutup [PDF 17 / cetak 16]. Setiap subbab berisi **minimum tiga paragraf** [PDF 20 / cetak 19].

- **Bab 1 Pendahuluan** memuat Latar Belakang, Rumusan Masalah, Ruang Lingkup, Tujuan Penelitian, Sistematika Penulisan [PDF 17 / cetak 16]. Latar belakang memuat alasan pemilihan topik dengan data relevan, memaparkan dari umum ke masalah yang diangkat, dan menyebut perbedaan dengan penelitian terdahulu. Rumusan masalah jelas, spesifik, terfokus, singkat, mencerminkan fokus latar belakang. Ruang lingkup membatasi variabel, data, metode, tools. Tujuan menggambarkan target capaian, naratif atau poin, sesuai rumusan masalah. Sistematika memaparkan gambaran bab ke bab secara narasi (bukan poin). Detail di `references/bab1-pendahuluan.md`.
- **Bab 2 Tinjauan Pustaka**: uraian sistematis landasan teori dan landasan empiris yang relevan, termasuk hasil penelitian terdahulu dengan sumber yang jelas [PDF 17 / cetak 16]. Syarat sumber bacaan: (a) terkait masalah yang dibahas; (b) kemutakhiran 10 tahun terakhir; (c) minimal 20 sumber, terdiri 70% artikel ilmiah dan 30% (buku, jurnal, prosiding, skripsi/tesis/disertasi, majalah akademik resmi, sumber online institusi resmi seperti BPS, kementerian, atau web .gov/.ac/.edu), bukan blog pribadi. Untuk perbandingan penelitian terdahulu dan sintesis gap, baca `references/penelitian-terdahulu.md`. Detail di `references/bab2-tinjauan-pustaka.md`.
- **Bab 3 Metode Penelitian**: uraian cara kerja dan teknik/proses pengerjaan, termasuk bahan dan peralatan (data, perangkat keras dan lunak, teori dan persamaan, teknik pengumpulan dan analisis data, model pendekatan, rancangan penelitian, cara penafsiran, ujicoba dan evaluasi, cara pengambilan kesimpulan) [PDF 17 / cetak 16]. Untuk informatika dapat diisi uraian peralatan, algoritma/metode, prosedur implementasi (Prototype, Waterfall, SDLC, Agile, SWDLC, Luther, CRISP-DM, dan sejenisnya), dan disajikan sebagai bagan atau gambar alur penelitian. Metode memengaruhi struktur Bab 4. Detail di `references/bab3-metode.md`.
- **Bab 4 Hasil dan Pembahasan**: temuan disusun menurut urutan tujuan penelitian, disertai pembahasan yang menginterpretasikan data secara kritis dan mendalam [PDF 18 / cetak 17]. Pembahasan menjelaskan makna hasil termasuk tabel dan gambar dengan narasi jelas, ringkas, padat; mengaitkan temuan dengan teori atau penelitian sebelumnya; menjelaskan perbedaan atau kesenjangan; menunjukkan kontribusi ilmiah. Detail di `references/bab4-hasil-pembahasan.md`.
- **Bab 5 Penutup**: Kesimpulan dan Saran [PDF 18 / cetak 17]. Kesimpulan menjawab rumusan masalah dan tujuan Bab 1 berdasarkan hasil penelitian, bukan perulangan Bab 4. Saran bersifat implikasi praktis atau teoritis kepada pihak tertentu (lembaga, praktisi, peneliti selanjutnya), konstruktif, realistis, aplikatif, dan berhubungan logis dengan kesimpulan. Detail di `references/bab5-penutup.md`.
- **Bagian Akhir**: Daftar Pustaka dan Lampiran [PDF 18 / cetak 17]. Lampiran berisi data atau pelengkap yang mengganggu kesinambungan pembacaan bila dimasukkan ke isi, dikelompokkan menurut jenis (jadwal, tabel, daftar pertanyaan, gambar, grafik, desain). Kode program pada lampiran ditulis 8 pt spasi tunggal, penomoran halaman `L-x` di tengah bawah.

## 4. Teknik penulisan: kertas, format, penomoran, gambar, tabel [PDF 19-20 / cetak 18-19]

- Kertas HVS putih polos 80 gram, ukuran A4 yang ditulis pedoman `21,5 cm x 29,7 cm` (ukuran A4 baku tidak sama persis; jangan menyembunyikan ketidakselarasan ini) [PDF 19 / cetak 18].
- Margin atas 4 cm, bawah 3 cm, kiri 4 cm, kanan 3 cm. Spasi 1,5 (khusus Abstrak dan Abstract 1 spasi). Font Times New Roman (untuk program boleh Courier New), rata kiri-kanan [PDF 19 / cetak 18].
- Ukuran huruf: Judul Bab 14 pt tebal kapital; Judul Subbab 12 pt tebal; isi 12 pt normal. Tidak ada indentasi paragraf kecuali dengan numbering [PDF 19 / cetak 18].
- Penomoran bab/subbab: angka latin mengacu induk (1, 1.1, 1.1.1); nomor dan judul bab di tengah, kapital, 14 pt tebal; nomor dan judul subbab dari kiri, kapital di awal kata, 12 pt tebal [PDF 19-20 / cetak 18-19]. Contoh: `2. JUDUL BAB`, `2.1. Judul Subbab`, `2.2.1. Judul Sub-Subbab`. Setiap subbab minimum tiga paragraf.
- Penomoran halaman: Bagian Awal angka Romawi kecil di tengah bawah (2 cm dari bawah); Halaman Judul dan Lembar Pengesahan tidak ditampilkan nomornya tetapi tetap dihitung. Bagian Pokok angka latin, halaman pertama bab pertama bernomor 1; halaman pertama tiap bab di tengah bawah, halaman lain di pojok kanan atas. Bagian Akhir angka latin di tengah, kelanjutan penomoran bagian pokok [PDF 20 / cetak 19].
- Gambar/tabel: judul gambar/grafik di bawah tengah; judul tabel di atas tengah; penomoran per bab (mis. `Gambar 3.1`, `Tabel 3.1`); tabel bersambung ke halaman berikutnya harus diulang headernya (`Repeat header`); gambar/tabel bukan buatan sendiri wajib melampirkan sitasi sumber; ukuran huruf 12 pt; semua gambar dan tabel dirujuk dalam tulisan dan dijelaskan [PDF 20 / cetak 19]. Klasifikasi tabel, diagram sistem (flowchart, UML, navigasi), screenshot antarmuka, dan grafik diatur di `references/visual-dan-lampiran-kode.md`.

## 5. Daftar pustaka dan sitasi [PDF 20 / cetak 19]

- Daftar Pustaka **wajib dibuat otomatis menggunakan tools** seperti bibliography, Mendeley, atau lainnya [PDF 20 / cetak 19].
- Format referensi **Harvard**; bila sitasi tidak lengkap atau tidak sesuai, wajib melengkapi dan menyesuaikan secara manual (panduan Harvard: https://lib.ugm.ac.id/en/harvard-referencing-style/ ). **Wajib mencantumkan DOI artikel.** Ditulis alfabetis; gelar tidak perlu dituliskan; setiap pustaka 1 spasi (rata kiri) dan jarak antarpustaka 2 spasi; semua nama penulis ditulis lengkap; tahun terbit disarankan minimal 10 tahun terakhir.
- Komposisi: 70% artikel ilmiah (jurnal) dan 30% (buku, prosiding, skripsi/tesis/disertasi, majalah akademik resmi, sumber online institusi resmi, bukan blog pribadi) [PDF 18 / cetak 17].
- Sitasi format Harvard dengan dasar `(Nama Belakang Penulis, Tahun)`. Bila baru pertama kali muncul, semua nama penulis disebutkan, mis. `(Sari, Jannah, Meuraxa, Syahfitri & Omar, 2022)`; selanjutnya boleh `(Sari et al., 2022)`. Sitasi dua penulis selalu disebutkan semuanya, mis. `(Susi dan Darujati, 2021)` [PDF 20 / cetak 19]. Detail pola per jenis sumber di `references/sitasi-dan-daftar-pustaka.md` dan contoh Lampiran 6.9.

## 6. Bahasa dan pengetikan [PDF 21 / cetak 20]

- Pengetikan memakai aplikasi text processing yang mendukung penulisan akademik terstruktur dan konsisten; aplikasi yang direkomendasikan adalah **LyX atau LaTeX** (mengatur otomatis format, sitasi, daftar pustaka, tabel, dan persamaan matematis) [PDF 21 / cetak 20]. Rekomendasi bukan larangan Word untuk draf, tetapi periksa ketentuan format pada tahap pengumpulan.
- Utamakan padanan Indonesia untuk kata asing. Istilah asing yang belum terserap dicetak miring, kecuali nama [PDF 14, 21 / cetak 13, 20].
- Gunakan kalimat deklaratif/informasi, bukan kalimat perintah. Hindari kata ganti orang dalam tubuh ilmiah. Jangan tulis singkatan seperti `dll`, `sbb`, `a.l`; uraikan. Singkatan lain dieja panjang saat pertama muncul diikuti singkatan dalam kurung.
- Seluruh naskah mengikuti kaidah etika penulisan ilmiah (lihat bagian 7).

## 7. Etika penulisan ilmiah [PDF 8-10 / cetak 7-9]

Etika penulisan ilmiah adalah norma atau standar aturan perilaku yang harus dilakukan (dan yang tidak boleh dilakukan) penulis tentang baik (dan buruknya) cara penulisan ilmiah. Lima sifat: (1) Kejujuran, (2) Bebas Plagiarisme, (3) Menjunjung Hak Cipta (UU No. 19 Tahun 2002), (4) Keabsahan, (5) Keterandalan [PDF 8-9 / cetak 7-8].

Enam bentuk pelanggaran: (1) Fabrikasi (merekayasa data yang tidak ada), (2) Falsifikasi (memanipulasi atau memalsukan data), (3) Plagiat (menjiplak karya orang lain tanpa atribusi), (4) Kepengarangan Tidak Sah (mencantumkan atau menghilangkan nama yang tidak/sudah berkontribusi), (5) Konflik Kepentingan (hasil dipengaruhi kepentingan pribadi/institusional), (6) Pengajuan Jamak (mengirim naskah sama ke lebih dari satu penerbit tanpa persetujuan) [PDF 9-10 / cetak 8-9]. Detail di `references/etika-dan-integritas.md`.

## 8. Alur penyelesaian dan administrasi non-sidang [PDF 22 / cetak 21]

Bagian ini merangkum alur bimbingan dan luaran resmi. Untuk panduan lengkap pendaftaran sidang BAAK, busana sidang, slide presentasi, simulasi tanya-jawab, dan penyelesaian matriks revisi pascasidang, baca `references/alur-sidang-dan-revisi.md`.

- Mahasiswa mendapat informasi nama dosen pembimbing pada modul akademik di Studentsite; Program Studi mengumumkan kontak pembimbing melalui email dan mahasiswa segera menghubungi pembimbing.
- Selama bimbingan, mahasiswa membawa buku agenda bimbingan skripsi yang dapat diunduh di https://fti.gunadarma.ac.id/informatika/?page_id=530 .
- Setelah mendapat persetujuan pembimbing, selain penulisan skripsi mahasiswa berkewajiban membuat **artikel ilmiah** dan **manual book** dari penulisan skripsi. Format dan rincian penyusunannya diatur di `references/artikel-ilmiah-dan-manual-book.md`.
- Detail administrasi bimbingan di `references/administrasi.md`.

## Ketidakselarasan yang tidak boleh disembunyikan

Baca `references/ketidakselarasan.md` untuk daftar konflik dan contoh. Jangan putuskan aturan dari satu contoh lampiran; catat dua halaman sumber dan tandai `pedoman ambigu` bila perlu konfirmasi.

## Verifikasi minimum sebelum menyatakan selesai

- Struktur bagian, semua komponen awal, lima bab isi, bagian akhir dan lampiran hadir sesuai relevansi; Daftar Isi serta daftar ilustrasi sesuai halaman sebenarnya.
- Latar belakang menjelaskan alasan dengan data dan pembanding penelitian terdahulu; rumusan masalah, ruang lingkup, tujuan, dan sistematika konsisten; setiap subbab minimum tiga paragraf.
- Bab 2 memuat landasan teori dan empiris dengan minimal 20 sumber (70% artikel ilmiah, 10 tahun terakhir); Bab 3 memaparkan metode yang dapat diulangi; Bab 4 menafsirkan hasil dan mengaitkan teori; Bab 5 menjawab rumusan masalah dan tidak mengulang Bab 4.
- Substansi riset diuji dengan `references/audit-substansi-informatika.md`: pencegahan kebocoran data (data leakage) dan metrik komprehensif untuk AI; sinkronisasi UML, skema DB, dan pengujian blackbox/SUS untuk rekayasa perangkat lunak; serta matriks traceability antar-bab.
- Format font, kertas, margin, spasi, judul bab/subbab, caption gambar/tabel, tabel bersambung, dan penomoran halaman diperiksa pada file sumber (DOCX atau LaTeX/LyX via `references/panduan-latex-lyx.md`) dan PDF final. Jalankan `python3 scripts/audit_skripsi.py <naskah>` untuk verifikasi otomatis awal.
- Abstrak dan Abstract masing-masing maksimum 250 kata, kata kunci, tahun Daftar Pustaka, dan hitungan halaman diperiksa; tidak ada nama, tanggal, atau tanda tangan yang direka.
- Daftar pustaka dibuat otomatis, Harvard, mencantumkan DOI, alfabetis, pasangan sitasi dan pustaka lengkap dua arah, serta memenuhi komposisi 70% artikel ilmiah.
- Saat melaporkan kepatuhan, beri status `sesuai / tidak sesuai / belum dapat diuji / pedoman ambigu` pada tiap poin; laporkan konflik dengan kedua halaman, bukan membuat ketentuan baru.

## Rujukan pendamping

- `references/cakupan-halaman.md`: peta seluruh 34 halaman pedoman ke bagian skill.
- `references/contoh-dan-lampiran.md`: 36 tema judul dan contoh Lampiran 6.1 sampai 6.9.
- `references/ketidakselarasan.md`: konflik internal pedoman dan contoh lampiran.
- `references/konflik-visual-lampiran.md`: tata letak contoh, ukuran terukur, dan perbedaan dengan ketentuan tertulis.
- `references/alur-audit.md`: input audit, pemeriksaan isi dan visual, format laporan.
- `references/draf-dokumen.md`: urutan draf lengkap, inden alinea, placeholder, cek DOCX/PDF.
- `references/bab1-pendahuluan.md`: isi dan kerangka Bab 1.
- `references/bab2-tinjauan-pustaka.md`: isi dan syarat Bab 2.
- `references/bab3-metode.md`: isi dan kerangka Bab 3.
- `references/bab4-hasil-pembahasan.md`: isi dan kerangka Bab 4.
- `references/bab5-penutup.md`: isi dan kerangka Bab 5.
- `references/penelitian-terdahulu.md`: tabel perbandingan dan sintesis gap.
- `references/sitasi-dan-daftar-pustaka.md`: Harvard, DOI, komposisi, contoh entri.
- `references/visual-dan-lampiran-kode.md`: tabel, diagram, grafik, lampiran kode.
- `references/pedoman-visual-dan-evaluasi.md`: UML, storyboard, navigasi, metodologi.
- `references/etika-dan-integritas.md`: lima sifat etika dan enam pelanggaran.
- `references/proposal-dan-alur-riset.md`: proposal, alur penyelesaian non-sidang, artikel ilmiah, manual book.
- `references/dataset-dan-reproduksibilitas.md`: sumber data, split, seed, ledger klaim.
- `references/administrasi.md`: agenda bimbingan dan kewajiban non-sidang.
- `references/alur-sidang-dan-revisi.md`: alur sidang BAAK, busana, slide presentasi, simulasi Q&A, dan matriks revisi.
- `references/artikel-ilmiah-dan-manual-book.md`: format dan struktur luaran wajib artikel ilmiah serta manual book.
- `references/audit-substansi-informatika.md`: audit substansi teknis AI/Data Science, Rekayasa Perangkat Lunak, dan matriks keterkaitan logika.
- `references/panduan-latex-lyx.md`: panduan template, konfigurasi preamble LaTeX dan pengaturan LyX standar Gunadarma.
- `references/glosarium-istilah-informatika.md`: kamus padanan baku komputasi dan istilah asing yang wajib dicetak miring.
- `references/panduan-pembuatan-dari-nol.md`: alur kerja 9 fase pembuatan skripsi dari nol bagi AI dan mahasiswa.
- `references/bagian-awal-naskah.md`: format detail setiap komponen sebelum Bab 1 (judul, pengesahan, orisinalitas, abstrak, pengantar, daftar isi).
- PDF pedoman asli: berkas resmi Prodi Informatika 2025, sumber primer untuk redaksi dan tampilan halaman. PDF tidak didistribusikan ulang dalam repo ini; jangan samakan ringkasan skill dengan naskah asli.
