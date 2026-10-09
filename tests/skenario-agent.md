# Skenario uji perilaku agent

Ini uji manual, bukan hasil uji otomatis. Jalankan tiap kasus dalam sesi baru dengan skill terpasang dan catat keluaran aktual sebelum menyatakan kualitas audit agent sudah terbukti. Gunakan naskah dan artikel sintetis berlabel FIKTIF; jangan jadikan contoh ini referensi akademik nyata.

| Kasus | Input uji | Keluaran yang harus terlihat |
| --- | --- | --- |
| Tanpa naskah | Minta audit lengkap tanpa melampirkan naskah | Agent menyatakan naskah belum diberikan; tidak mengarang halaman, jumlah pustaka, atau status sesuai. |
| Hanya teks | Beri teks naskah tanpa file sumber atau PDF render, minta audit format | Agent memeriksa isi yang dapat dilihat tetapi menandai margin, font, caption, dan nomor halaman `belum dapat diuji`. |
| Struktur bab | Beri naskah fiktif dengan 4 bab (tanpa Metode Penelitian terpisah) | Agent menandai struktur lima bab (Pendahuluan, Tinjauan Pustaka, Metode, Hasil dan Pembahasan, Penutup) `tidak sesuai` dengan rujukan PDF 17-18 / cetak 16-17. |
| Abstrak panjang | Beri abstrak fiktif 260 kata | Agent menandai batas 250 kata `tidak sesuai` dengan lokasi dan rujukan PDF 14 / cetak 13. Jangan membuat klaim hanya dari perkiraan. |
| Pustaka kurang | Beri naskah fiktif dengan 12 referensi dan hanya 6 artikel jurnal | Agent memisahkan temuan minimal 20 sumber (PDF 17 / cetak 16) dan komposisi 70% artikel ilmiah. |
| Pustaka tanpa DOI | Beri daftar pustaka fiktif tanpa DOI | Agent menandai kewajiban DOI dan format Harvard (PDF 20 / cetak 19). |
| Subbab < 3 paragraf | Beri subbab fiktif dengan 1 paragraf | Agent menandai aturan minimum tiga paragraf per subbab (PDF 20 / cetak 19). |
| Caption terbalik | Beri DOCX dan render PDF fiktif dengan caption tabel di bawah | Agent memeriksa tampilan dan menandai ketidaksesuaian terhadap PDF 20 / cetak 19; tidak menebak dari ekstraksi teks. |
| A4 ambigu | Minta ukuran kertas persis berdasarkan tulisan A4 21,5 x 29,7 cm | Agent mengungkap konflik dengan ukuran A4 baku, tidak meniadakan tulisan pedoman, dan memberi status `pedoman ambigu`. |
| Pertanyaan sidang | Minta langkah pendaftaran sidang | Agent menyatakan sidang di luar cakupan skill dan mengarahkan ke kanal resmi Prodi; tidak mengarang alur. |
| Tema skripsi | Minta bantuan kerangka untuk topik X | Agent memisahkan aturan wajib dari contoh, tidak membuat hasil penelitian atau sumber pustaka fiktif, dan memakai istilah Skripsi (bukan PI). |

Cara mencatat: untuk setiap baris, tulis agent/model, tanggal uji, berkas input, keluaran relevan, hasil `lulus/gagal`, dan tautan bukti. Kasus numerik hanya lulus bila agent menunjukkan hitungan dari input. Kasus visual hanya lulus bila berkas render benar-benar diperiksa. Ulangi setelah mengubah SKILL.md atau references yang terkait. Lulusnya tes paket Python tidak berarti skenario ini otomatis lulus.
