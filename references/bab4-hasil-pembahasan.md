# Bab 4 Hasil dan Pembahasan: isi dan kerangka

Bab 4 menyajikan temuan penelitian yang disusun berdasarkan urutan tujuan penelitian, disertai pembahasan yang menginterpretasikan data secara kritis dan mendalam [PDF 18 / cetak 17]. Pembahasan harus menjelaskan makna hasil penelitian termasuk tabel dan gambar dengan narasi yang jelas, ringkas, dan padat. Penulis mengaitkan temuan dengan teori atau penelitian sebelumnya, menjelaskan perbedaan atau kesenjangan, dan menunjukkan kontribusi ilmiah.

## Prinsip penyajian

1. **Ikuti urutan tujuan** yang ditetapkan di Bab 1, bukan urutan kegiatan secara acak.
2. **Setiap tabel dan gambar wajib dirujuk** dalam teks dengan nomornya (mis. `...sebagaimana ditunjukkan pada Tabel 4.1...`) dan diberi penjelasan. Jangan meletakkan visual tanpa narasi pengantar.
3. **Interpretasi kritis**: bukan sekadar menampilkan angka, tetapi menjelaskan makna, sebab, dan implikasinya.
4. **Kaitkan dengan teori dan penelitian terdahulu**: bandingkan hasil dengan Bab 2 dan penelitian sebelumnya; jelaskan persamaan, perbedaan, dan kesenjangan.
5. **Tunjukkan kontribusi ilmiah** yang benar-benar terlaksana; hindari klaim universal tanpa bukti.

## Struktur yang lazim (pilih sesuai jenis penelitian)

- Untuk penelitian komparatif/eksperimen: `4.1 Gambaran Umum Eksperimen`, `4.2 Hasil Pra-pemrosesan dan Rekayasa Fitur`, `4.3 Perbandingan Performa Model` (optimasi hyperparameter, evaluasi metrik, validasi cross-validation, uji signifikansi, trade-off efisiensi), `4.4 Analisis Interpretabilitas`, `4.5 Implikasi / Keterbatasan`.
- Untuk pengembangan aplikasi: `4.1 Hasil Implementasi`, `4.2 Tampilan Antarmuka`, `4.3 Pengujian` (fungsional black-box, pengujian akurasi/kinerja), `4.4 Pembahasan`.
- Untuk perancangan: `4.1 Hasil Rancangan`, `4.2 Evaluasi Rancangan`, `4.3 Pembahasan`.

## Penyajian hasil kuantitatif

- Gunakan tabel hasil evaluasi dengan metrik yang relevan (akurasi, presisi, recall, F1, AUC-ROC, mAP, WER, latensi) dan nilai rata-rata/minimum/maksimum/standar deviasi bila ada.
- Sertakan grafik hanya bila membantu pemeriksaan angka (mis. perbandingan antar model). Ikuti `references/visual-dan-lampiran-kode.md`: grafik hitam-putih kontras tinggi, mulai dari nol, label angka langsung.
- Setiap angka berasal dari hasil eksekusi nyata dan dapat dilacak ke berkas mentah. Jangan mengarang angka.

## Pembahasan dan kontribusi

- Jelaskan mengapa hasil demikian terjadi, bukan hanya melaporkan angka.
- Bandingkan dengan hasil penelitian terdahulu: lebih baik, setara, atau berbeda, dan mengapa (dataset, protokol, metode).
- Nyatakan keterbatasan penelitian secara jujur (mis. ukuran data, cakupan, asumsi) tanpa menutupi.
- Rumuskan kontribusi secara terbatas dan dapat dipertanggungjawabkan; gunakan `pada studi yang ditelaah` bila cakupan terbatas.

## Aturan penulisan

- Kalimat deklaratif, bukan perintah; hindari kata ganti orang.
- Nomor tabel/gambar per bab (mis. `Tabel 4.1`, `Gambar 4.2`); judul tabel di atas tengah, judul gambar di bawah tengah; ukuran huruf 12 pt.
- Tabel bersambung ke halaman berikutnya harus mengulang header dan diberi penanda `Lanjutan Tabel 4.x`.
- Setiap subbab minimum tiga paragraf.

## Verifikasi Bab 4

- Temuan disusun mengikuti urutan tujuan Bab 1.
- Setiap tabel/gambar dirujuk dan dijelaskan; tidak ada visual menggantung.
- Interpretasi kritis dan dikaitkan dengan teori serta penelitian terdahulu.
- Angka dapat dilacak ke berkas hasil; tidak ada angka rekaan.
- Keterbatasan dan kontribusi dinyatakan dengan batas klaim yang jujur.
