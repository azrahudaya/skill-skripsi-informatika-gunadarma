# Visual, tabel, diagram, dan lampiran kode

Gunakan panduan ini saat naskah memuat tabel data, diagram alur, arsitektur sistem, rancangan antarmuka, grafik numerik, atau listing program. Pedoman Skripsi 2025 mengatur posisi caption, penomoran, dan pengulangan header tabel [PDF 20 / cetak 19] serta memperbolehkan kode program pada lampiran dengan ukuran 8 pt spasi tunggal [PDF 18 / cetak 17]. Grafik dan diagram bukan wajib ada pada setiap subbab; pedoman tidak mensyaratkannya. Pilih visual hanya bila membantu pembaca memeriksa angka, alur pemrosesan, atau perbandingan. Jangan mengisi halaman demi ketebalan naskah.

## 1. Aturan penomoran, caption, dan rujukan naskah

1. Penomoran berbasis bab: `[Nomor Bab].[Nomor Urut]`, mis. `Gambar 3.1` (gambar pertama Bab 3), `Tabel 2.2`. Penomoran diulang dari angka 1 pada setiap bab [PDF 20 / cetak 19].
2. Posisi dan tipografi caption:
   - Caption tabel: **atas tengah** tabel. Times New Roman 12 pt, spasi tunggal mulai judul tabel hingga isi [PDF 20 / cetak 19].
   - Caption gambar: **bawah tengah** gambar. Times New Roman 12 pt, spasi tunggal, simetris terhadap gambar.
3. Rujukan wajib dalam teks: setiap gambar dan tabel WAJIB dirujuk dengan menyebut nomornya, mis. `...seperti ditunjukkan pada Gambar 3.1...`. Dilarang `gambar di atas`, `tabel di bawah`, atau visual menggantung tanpa narasi.
4. Sumber kutipan: bila gambar/tabel diambil atau diadaptasi dari karya pihak ketiga, cantumkan sumber pada akhir caption atau di bawah tabel dengan format `(Sumber: Penulis, Tahun)`. Untuk karya mandiri, cukup sebut sumber data pada teks pengantar.
5. Sinkronisasi daftar awal: semua judul dan nomor pada caption harus sinkron persis dengan entri pada Daftar Tabel dan Daftar Gambar, termasuk nomor halaman hasil render akhir [PDF 16 / cetak 15].

## 2. Format dan anatomi tabel akademik FTI

1. Garis: gunakan gaya tabel formal tiga garis batas horizontal utama (atas, pemisah kepala kolom, bawah). Hindari garis vertikal tebal atau kisi kotak yang melelahkan mata, kecuali tabel formulir tertentu.
2. Judul kolom (header) dicetak normal, tidak tebal. Spasi di dalam sel 1. Font dalam tabel Times New Roman 10 pt atau 11 pt (dapat diperkecil hingga 9 pt pada tabel padat agar muat dalam lebar margin) [PDF 20 / cetak 19].
3. Perataan sel: kolom teks/nama rata kiri; kolom nomor/status/simbol rata tengah; kolom angka rata kanan atau rata tengah berpatokan tanda desimal.
4. Tabel bersambung lintas halaman: judul tabel dan kepala kolom harus muncul pada halaman sambungan. Di Word gunakan `Table Properties > Row > Repeat as header row at the top of each page`; cantumkan teks `Lanjutan Tabel 3.x Judul Tabel` di atas tabel sambungan [PDF 20 / cetak 19].

## 3. Jenis tabel umum dalam Skripsi Informatika

1. Spesifikasi perangkat keras dan lunak (Bab 3): kolom Komponen, Spesifikasi, Keterangan.
2. Kamus data / skema basis data (Bab 3): kolom Nama Kolom, Tipe Data, Panjang, Keterangan/Constraint.
3. Matriks penelitian terdahulu / state of the art (Bab 2): kolom Peneliti & Tahun, Objek/Dataset, Metode & Model, Metrik & Hasil, Celah (lihat `references/penelitian-terdahulu.md`).
4. Skenario pengujian / test case (Bab 3-4): kolom Nomor Kasus, Fitur/Skenario, Masukan, Luaran Diharapkan, Kondisi Batas.
5. Hasil evaluasi dan metrik kinerja (Bab 4): kolom Metrik, Nilai Rata-rata, Minimum, Maksimum, Standar Deviasi.
6. Simbol notasi standar (Bab 2-3): kolom Simbol, Nama Notasi, Deskripsi.

## 4. Diagram dan standar pemodelan sistem

1. Flowchart: simbol baku ISO/ANSI (terminator elips untuk awal/akhir, proses persegi panjang, keputusan belah ketupat, input/output jajar genjang, konektor lingkaran). Arah panah tegas, tidak bercabang tanpa blok keputusan.
2. UML: Use Case Diagram (batas sistem kotak, aktor, use case elips, include/extend garis putus-putus berarah); Activity Diagram (status awal lingkaran solid, aktivitas persegi berujung bulat, keputusan belah ketupat, swimlane vertikal, status akhir lingkaran cincin); Class/ERD (entitas, atribut, relasi kardinalitas 1:1, 1:N, M:N).
3. Struktur navigasi sistem: linier, non-linier, hierarki, campuran/komposit.
4. Diagram arsitektur/blok sistem: hubungan antarkomponen (sensor IoT, gateway, cloud API, basis data, aplikasi) dengan label modul, protokol komunikasi, dan arah aliran data.

## 5. Tangkapan layar dan grafik eksperimen

1. Tangkapan layar: tampilkan antarmuka yang mewakili alur kerja (formulir utama, hasil keluaran, pesan status). Teks harus tajam dan terbaca pada skala cetak. Beri garis tepi tipis bila latar putih. Gunakan fitur screenshot bawaan, bukan foto layar monitor.
2. Grafik kuantitatif: gunakan data asli; pertahankan satuan, urutan label, dan jumlah sampel. Default hitam putih/abu-abu kontras tinggi berlatar putih, tanpa warna bawaan, gradien, atau efek 3D. Pembedaan seri harus bertahan saat difotokopi (label langsung, pola garis putus-putus, arsiran, penanda titik). Satu grafik satu pertanyaan; sumbu kuantitas mulai dari nol. Keluaran PNG resolusi tinggi (minimal 1600 piksel sisi panjang atau 300 DPI) atau vektor.

## 6. Lampiran listing program

1. Tentukan seluruh kode yang benar-benar dipakai untuk hasil yang dilaporkan: skrip utama, prapemrosesan, konfigurasi nonrahasia, analisis lanjutan, pembuat grafik, penguji. Berkas sumber elektronik tetap disertakan dengan manifest nama, versi, peran, dan hash. Jangan sertakan lingkungan virtual, paket pihak ketiga, cache, dataset pribadi, token, atau kredensial.
2. Masukkan kode relevan ke lampiran dalam urutan logis, satu judul lampiran per berkas, dengan nomor baris bila memungkinkan, font monospasi 8 pt spasi tunggal [PDF 18 / cetak 17]. Jika kode terlalu besar untuk berkas cetak, jelaskan pemisahan: lampiran cetak berisi kode untuk mereproduksi hasil utama, arsip elektronik menyimpan seluruh kode; jangan mengklaim lampiran cetak berisi semuanya jika tidak.
3. Lindungi sumber dari perubahan perilaku: ekstrak teks lampiran PDF dan bandingkan baris nonkosong dengan berkas sumber asli dalam urutan sama; token, string, parameter, dan urutan blok tidak boleh hilang. Simpan hash dan hasil uji dalam laporan verifikasi.
4. Lakukan eksekusi ulang kode terhadap input tetap, cocokkan keluaran mentah dengan tabel/grafik pada naskah, catat lingkungan perangkat lunak. Jangan menyamakan kode yang terlihat benar dengan hasil yang benar-benar dijalankan.
5. Setelah render, audit nomor halaman `L-1`, `L-2` dan seterusnya, Daftar Lampiran, header per berkas, serta tidak ada potongan kode yang tertinggal di luar halaman.

## 7. Bukti minimum saat menyerahkan

Laporkan untuk setiap visual: tujuan, sumber data, skrip, kesamaan angka dengan output, ukuran cetak, dan lokasi halaman. Untuk lampiran: daftar berkas, hash, cakupan kode tercetak dan elektronik, hasil eksekusi ulang, kesamaan isi lampiran dengan sumber, dan status pemeriksaan PDF akhir. Jika sumber Word asli tidak tersedia, nyatakan bahwa DOCX belum diverifikasi dengan Word, lalu jangan menyamakan render Chrome/LibreOffice dengan hasil cetak Word.
