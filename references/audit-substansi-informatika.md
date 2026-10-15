# Audit Substansi Riset Informatika

Selain format fisik dan tata letak dokumen, keberhasilan skripsi Informatika di Universitas Gunadarma ditentukan oleh kedalaman substansi teknis dan konsistensi logika ilmiah antar-bab.

## 1. Audit Jalur AI / Data Science / Machine Learning / Deep Learning

### A. Dataset dan Pra-Pemrosesan
- **Asal Usul Data (Provenance)**: Sumber dataset wajib jelas (tautan resmi repositori publik seperti Kaggle/UCI, API resmi, atau izin pengambilan data primer).
- **Distribusi dan Imbalance**: Laporkan jumlah sampel per kelas. Jika terjadi ketimpangan kelas ekstrem (class imbalance), wajib dipaparkan teknik penanganannya (SMOTE, random over/undersampling, focal loss, atau penyesuaian bobot kelas).
- **Pencegahan Kebocoran Data (Data Leakage Defense)**:
  * Pembagian dataset (train/val/test split) WAJIB dilakukan sebelum langkah normalisasi (MinMax, StandardScaler), imputasi nilai hilang, atau seleksi fitur.
  * Fit transform hanya dipelajari pada data latih, lalu transform diaplikasikan ke data validasi dan uji.
  * Jika menggunakan Cross-Validation, proses pipeline scaling wajib berada di dalam loop lipatan (folds).

### B. Evaluasi dan Metrik Performa
- **Hindari Ilusi Akurasi**: Jangan hanya mengandalkan nilai Accuracy tunggal, terutama pada dataset tidak seimbang.
- **Kelengkapan Metrik Klasifikasi**: Wajib menyajikan Precision, Recall, F1-Score (macro/weighted), dan Confusion Matrix visual.
- **Metrik Regresi**: Sajikan MAE, RMSE, dan R-squared (atau MAPE jika data non-nol).
- **Metrik Deteksi Objek / Segmentasi**: Gunakan mAP@0.5, mAP@0.5:0.95, IoU, atau Dice Coefficient.
- **Perbandingan Baseline**: Model yang diajukan wajib dikomparasi secara adil terhadap model dasar (baseline) atau penelitian terdahulu yang menggunakan dataset identik.

### C. Keterulangan (Reproducibility)
- Catat parameter hiper (learning rate, batch size, epoch, optimizer, activation function).
- Catat random state / seed yang digunakan.
- Cantumkan spesifikasi lingkungan perangkat keras (tipe GPU, CPU, RAM) dan waktu komputasi pelatihan (training time).

---

## 2. Audit Jalur Rekayasa Perangkat Lunak / Web / Mobile / IoT

### A. Sinkronisasi Diagram Rekayasa Sistem (UML)
- **Use Case Diagram**: Setiap use case harus memiliki aktor yang jelas dan skenario tekstual (use case description) yang memuat skenario normal dan alternatif.
- **Activity Diagram**: Setiap activity diagram harus merefleksikan alur langkah pada salah satu use case.
- **Sequence Diagram**: Aktor dan objek pada sequence diagram harus selaras dengan class diagram dan boundary-control-entity.
- **Class Diagram**: Relasi antar-kelas (asosiasi, agregasi, komposisi, inheritance) serta atribut dan operasi harus sesuai dengan rancangan modul program.
- **ERD ke Skema Basis Data**: Kardinalitas relasi entitas pada ERD wajib konsisten dengan foreign key pada tabel fisik di database (termasuk normalisasi 1NF, 2NF, dan 3NF).

### B. Pengujian Fungsional dan Non-Fungsional
- **Blackbox Testing**: Tabel pengujian blackbox harus memuat skenario uji, data masukan, hasil yang diharapkan, hasil pengamatan aktual, dan status (valid/tidak valid). Gunakan teknik Equivalence Partitioning dan Boundary Value Analysis.
- **User Acceptance Testing (UAT)**: Melibatkan responden pengguna nyata dengan skenario tugas yang terukur.
- **System Usability Scale (SUS)**: Jika melakukan evaluasi kepuasan pengguna dengan SUS (10 pertanyaan skala Likert 1-5), gunakan rumus pembobotan baku:
  * Pertanyaan ganjil: Skor skala dikurangi 1.
  * Pertanyaan genap: 5 dikurangi skor skala.
  * Jumlahkan total bobot lalu kalikan 2.5 (skor akhir 0 sampai 100). Bandingkan dengan rata-rata industri (skor 68).

### C. Khusus Perangkat Keras dan IoT
- Diagram blok arsitektur perangkat keras: sensor, mikrokontroler (ESP32/Arduino/Raspberry Pi), aktuator, dan sumber daya.
- Skema pengkabelan / wiring diagram dan topologi komunikasi (MQTT, HTTP REST, WebSockets).
- Parameter latensi transmisi data dan keandalan pembacaan sensor (packet loss, error tolerance).

---

## 3. Matriks Penyelarasan Logika Antar-Bab (Traceability Matrix)

Kelemahan paling sering pada skripsi Informatika adalah ketidaksinkronan antara masalah yang ditanyakan dengan hasil yang dilaporkan. Lakukan audit rantai benang merah berikut:

| Elemen Naskah | Titik Pemeriksaan | Indikator Keselarasan |
|---|---|---|
| Bab 1: Rumusan Masalah | Apakah dinyatakan dalam kalimat tanya/fokus yang jelas? | Misal ada 2 butir rumusan masalah. |
| Bab 1: Batasan Masalah | Apakah membatasi ruang lingkup yang relevan? | Membatasi dataset, platform, atau algoritma. |
| Bab 1: Tujuan Penelitian | Apakah menjawab secara simetris rumusan masalah? | Wajib ada 2 butir tujuan yang berpasangan 1-to-1 dengan rumusan masalah. |
| Bab 3: Metode Penelitian | Apakah memuat langkah teknis untuk mencapai tujuan tersebut? | Tahapan kerja mencakup proses pengolahan dan evaluasi yang terarah ke tujuan. |
| Bab 4: Hasil & Pembahasan | Apakah menyajikan data pembuktian dari setiap tujuan? | Setiap tujuan dibahas secara tuntas dengan tabel, grafik, atau evaluasi empiris. |
| Bab 5: Kesimpulan | Apakah menyimpulkan jawaban nyata, bukan sekadar teori umum? | Memuat 2 butir kesimpulan yang menyebutkan angka performa atau fakta keberhasilan sistem. |

Jika rumusan masalah menanyakan "Berapa tingkat akurasi model X?", maka kesimpulan di Bab 5 tidak boleh hanya menulis "Model X berhasil dibuat", melainkan wajib menulis "Model X menghasilkan akurasi 92.4% dan F1-Score 91.8% pada data uji".
