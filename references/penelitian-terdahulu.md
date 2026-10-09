# Penelitian terdahulu dan tabel perbandingan

Gunakan panduan ini saat menyusun Bab 2, terutama bila pengguna meminta perbandingan penelitian, *state of the art*, celah penelitian, atau tabel. Pedoman Skripsi 2025 mewajibkan Bab 2 memuat landasan teori dan landasan empiris dengan minimal 20 sumber (70% artikel ilmiah, 10 tahun terakhir) [PDF 17 / cetak 16], tetapi tidak mewajibkan judul `State of the Art`, jumlah baris tertentu, ataupun tabel dengan kolom baku. Bentuk tabel adalah pilihan penjelasan, bukan aturan universitas. Nomor `Tabel 2.1` di bawah hanya berlaku jika tabel itu memang tabel pertama Bab 2.

## Apa yang perlu dijaga

- Jangan menyalin identitas mahasiswa, hasil eksperimen, nilai metrik, nama pembimbing, atau rumusan klaim kebaruan dari naskah contoh. Nilai sebuah tabel datang dari kecocokan dan verifikasi studi, bukan jumlah barisnya.
- Artikel metode yang tidak membahas objek yang sama boleh dipakai untuk teori, tetapi jangan dimasukkan sebagai penelitian sejenis hanya untuk memenuhi kuota.
- Contoh naskah mahasiswa menempatkan subbagian `Penelitian Terdahulu` atau `State of the Art` dengan kolom seperti `No`, `Peneliti & Tahun`, `Judul`, `Metode`, `Hasil`, `Gap/Perbedaan`. Ini contoh tata urut, bukan izin menyalin klaim, tabel, atau sumbernya tanpa membaca artikel asli.

## Prosedur kajian yang dapat diuji

1. Rumuskan pertanyaan pembanding sebelum mencari artikel: objek/dataset, masalah, metode, fitur, cara membagi data, metrik, dan batasan yang membedakan penelitian saat ini. Sebutkan varian dataset bila relevan (mis. `bank-full.csv` vs `bank-additional.csv`), karena nama umum tidak menjamin ukuran dan kolom sama.
2. Temukan kandidat artikel jurnal/prosiding yang dekat dengan masalah dan metode; verifikasi penulis, tahun, judul, venue, halaman, DOI pada laman penerbit, Crossref, atau repositori institusi. Metadata membuktikan identitas publikasi, bukan hasil eksperimennya.
3. Baca teks lengkap, minimal abstrak, bagian data, metode, evaluasi, tabel hasil, dan pembahasan, sebelum menulis sel metode atau hasil. Simpan ledger privat `klaim | kutipan singkat | halaman/bagian artikel | DOI/URL | status teks penuh`. Jangan memasukkan salinan penuh artikel ke repo skill. Jika hanya metadata atau abstrak tersedia, tulis `belum terverifikasi dari teks lengkap`; jangan buat angka, desain uji, atau gap spesifik dari dugaan.
4. Pilih studi yang berbeda secara bermakna, bukan studi sebanyak mungkin. Untuk tiap studi, cek apakah dataset sama, atribut yang dipakai, split acak atau temporal, model yang dibandingkan, kelas positif yang dilaporkan, dan apakah nilai yang dikutip berasal dari uji akhir atau pelatihan. Bila artikel ambigu atau bertentangan, catat keterbatasannya tanpa menuduh kesalahan pasti.
5. Tulis paragraf pengantar yang menghubungkan pertanyaan penelitian dengan studi, lalu tabel yang muat di halaman. Skema ringkas: `Peneliti (tahun) | Data/objek | Metode dan evaluasi | Hasil yang diverifikasi | Perbedaan terhadap penelitian ini`. Jika tabel melebar, gunakan dua tabel pendek atau uraian setelah tabel; jangan mengecilkan font semua sel hingga tak terbaca. `Tabel 2.1` adalah caption di atas, tengah, dengan nomor bab; sebut tabel dengan nomornya pada teks. Bila melewati halaman, cek judul dan kepala tabel pada setiap halaman.
6. Setelah tabel, tulis analisis sintesis, bukan satu kalimat `berbeda dari penelitian sebelumnya`: apa yang sama, apa yang berbeda, mengapa protokol tidak bisa dibandingkan langsung, apa yang belum diuji, dan kontribusi yang memang terlaksana. Hindari klaim `belum ada penelitian` tanpa pencarian literatur yang cukup. Gunakan kata `pada studi yang ditelaah` jika cakupan terbatas.
7. Cocokkan setiap baris dengan sitasi di teks dan entri daftar pustaka, lalu audit kembali format halaman, Daftar Tabel, dan bukti sumber. Status `belum terverifikasi` yang memengaruhi kesimpulan tetap terbuka, bukan diluluskan diam-diam.

## Contoh struktur isi yang jujur

Paragraf pembuka: `Tabel 2.1 membandingkan penelitian terdahulu menurut varian data, cara evaluasi, dan ukuran kinerja. Rincian hanya dinyatakan ketika teks lengkap studi telah diperiksa.`

| Peneliti (tahun) | Data/objek | Metode dan evaluasi | Hasil yang diverifikasi | Perbedaan terhadap penelitian ini |
| --- | --- | --- | --- | --- |
| Studi A (tahun) | Nama/versi data dari artikel | Model, split dan metrik dari teks penuh | Angka atau temuan yang dapat dilacak ke tabel/halaman artikel | Beda dataset, atribut, split, atau tujuan yang faktual |
| Studi B (tahun) | Belum terverifikasi | Belum terverifikasi dari teks lengkap | Belum terverifikasi | Jangan merumuskan gap spesifik dari judul saja |
| Penelitian ini | Data dan jumlah baris dari eksperimen nyata | Kode, split, metrik yang dijalankan | Hasil dari berkas mentah yang dapat diulang | Kontribusi prosedural yang teruji; bukan klaim universal |

Isi contoh di atas adalah label format, bukan studi atau hasil nyata. Untuk draf yang belum mempunyai teks lengkap, tampilkan sel belum terverifikasi sebagai pekerjaan tertunda atau keluarkan barisnya. Jangan mengisi placeholder dengan sitasi palsu.

## Verifikasi sebelum menyerahkan

- Bab 2 memenuhi minimal 20 sumber dengan komposisi 70% artikel ilmiah, 10 tahun terakhir [PDF 17 / cetak 16].
- Setiap sel fakta tabel punya bukti sumber; bedakan metadata, abstrak, dan teks lengkap. Tidak ada angka kinerja dari judul atau cuplikan pencarian.
- Pembanding memakai dataset dan metrik yang jelas; nilai dari varian data atau skema uji berbeda tidak disandingkan sebagai kompetisi langsung.
- Tabel 2.1 hadir pada Daftar Tabel dengan halaman hasil render sebenarnya; caption di atas tengah; kepala tabel dan judul lintas halaman dicek pada PDF final.
- Paragraf pascatabel menjelaskan posisi dan gap dengan batas klaim yang jujur. Jika tidak ada gap yang kuat, nyatakan replikasi/perbandingan terbatas, bukan kebaruan palsu.
