# Bab 3 Metode Penelitian: isi dan kerangka

Bab 3 menguraikan cara kerja dan teknik/proses pengerjaan penelitian [PDF 17 / cetak 16]. Cakupannya meliputi: bahan dan peralatan (data, hasil penelitian lain, perangkat keras dan lunak, teori dan persamaan), teknik pengumpulan dan analisis data, model pendekatan, rancangan penelitian, cara penafsiran dan pengumpulan hasil, ujicoba dan cara evaluasi, serta cara pengambilan kesimpulan.

Untuk penelitian ilmu komputer/informatika, bab ini dapat diisi uraian peralatan yang dibutuhkan, algoritma/metode yang digunakan, prosedur implementasi (Prototype, Waterfall, SDLC, Agile, SWDLC, Luther untuk multimedia, CRISP-DM, dan sejenisnya), serta disajikan sebagai **bagan atau gambar alur penelitian**. Metode penelitian memengaruhi struktur dan sistematika pembahasan pada Bab 4 [PDF 17 / cetak 16].

Metode harus sesuai dan relevan dengan permasalahan, topik/tema, serta teori yang digunakan.

## Memilih kerangka prosedur sesuai jenis penelitian

Pedoman menyebut beberapa kerangka prosedur sebagai contoh, bukan kewajiban satu metode tertentu [PDF 17 / cetak 16]. Pilih yang benar-benar dipakai:

- **CRISP-DM** (Cross-Industry Standard Process for Data Mining): untuk penelitian berbasis data, klasifikasi, prediksi, analisis. Enam tahap: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment. Lazim untuk topik machine learning/data mining.
- **SDLC / Waterfall**: untuk pengembangan aplikasi/sistem dengan kebutuhan yang relatif tetap. Tahap: Analisis Kebutuhan, Perancangan, Implementasi, Pengujian, Pemeliharaan.
- **Prototype**: untuk pengembangan aplikasi yang memerlukan iterasi umpan balik pengguna. Siklus: Planning, Modeling, Construction, Deployment, Communication, berulang hingga memadai.
- **Agile / Scrum**: untuk pengembangan iteratif dengan sprint.
- **SWDLC** (Software Development Life Cycle) atau **Luther** (untuk aplikasi multimedia): sesuai objek.

Contoh struktur yang lazim (dari naskah nyata, hanya pola, bukan aturan): `3.1 Tahapan Penelitian`, `3.2 Analisis Kebutuhan`, `3.3 Perancangan Sistem`, `3.4 Implementasi`, `3.5 Pengujian`. Untuk CRISP-DM: `3.1 Business Understanding`, `3.2 Data Understanding`, `3.3 Data Preparation`, `3.4 Modeling`, `3.5 Evaluation`. Untuk penelitian komparatif model: `3.1 Jenis dan Pendekatan Penelitian`, `3.2 Alur Penelitian`, `3.3 Data Penelitian`, `3.4 Pra-pemrosesan Data`, `3.5 Pembangunan Model`, `3.6 Metode Evaluasi`, `3.7 Perangkat Lunak dan Perangkat Keras`.

## Subbagian yang lazim (pilih sesuai kebutuhan)

- **Jenis dan pendekatan penelitian**: eksperimen, studi kasus, pengembangan, atau komparatif; kuantitatif/kualitatif.
- **Alur / tahapan penelitian**: bagan dan narasi urutan kegiatan; gambar alur penelitian.
- **Data penelitian**: sumber data (primer/sekunder), deskripsi dan karakteristik dataset, jumlah observasi, variabel/fitur, kelas target. Untuk data sekunder, sebutkan asal dan lisensi. Ikuti `references/dataset-dan-reproduksibilitas.md`.
- **Pra-pemrosesan data**: pembersihan, penanganan nilai hilang, penanganan anomali, rekayasa fitur, pembagian data (train/validation/test, stratified), penanganan ketidakseimbangan kelas.
- **Perancangan sistem**: kebutuhan fungsional dan nonfungsional, arsitektur, pemodelan (UML: use case, activity, class; flowchart; struktur navigasi). Ikuti `references/pedoman-visual-dan-evaluasi.md`.
- **Pembangunan / implementasi**: algoritma dan model, arsitektur eksperimen, optimasi hyperparameter, pipeline.
- **Metode evaluasi**: metrik (akurasi, presisi, recall, F1, AUC-ROC, PR-AUC, mAP, WER, latensi), skema validasi (k-fold cross validation), uji signifikansi statistik bila ada.
- **Perangkat lunak dan perangkat keras**: lingkungan pengembangan, daftar perangkat lunak (versi) dan perangkat keras (spesifikasi). Sajikan sebagai tabel.

## Aturan penulisan

- Ditulis kronologis dan sistematis sehingga orang lain dapat mengulangi penelitian.
- Kalimat deklaratif, bukan perintah. Jangan mengarang tahap atau hasil yang tidak dilakukan.
- Alur penelitian disajikan sebagai gambar bernomor (mis. `Gambar 3.1`) dan dirujuk dalam teks.
- Setiap subbab minimum tiga paragraf.

## Verifikasi Bab 3

- Metode sesuai dan relevan dengan masalah, topik, dan teori.
- Tahapan lengkap dan dapat direplikasi; ada bagan/gambar alur penelitian.
- Data, pra-pemrosesan, model, dan evaluasi terdokumentasi; pembagian data dan seed jelas.
- Perangkat lunak dan perangkat keras dicantumkan.
- Tidak ada tahap atau hasil yang direkayasa; setiap angka dapat dilacak.
