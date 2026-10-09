# Dataset dan reproduksibilitas penelitian

Referensi ini membantu Bab 3 (Metode) dan Bab 4 (Hasil dan Pembahasan) agar data, eksperimen, dan angka hasil dapat ditelusuri dan diulang. Pedoman tidak menetapkan format baku untuk dokumentasi dataset, tetapi menuntut metode yang dapat diulangi dan data yang dapat dipertanggungjawabkan [PDF 17 / cetak 16].

## Sumber data

- **Data primer**: dikumpulkan sendiri (kuesioner, wawancara, sensor, pengukuran, observasi). Dokumentasikan instrumen, jumlah responden, periode, dan prosedur.
- **Data sekunder**: dari sumber publik atau institusi (mis. UCI, Kaggle, BPS, kementerian, repositori institusi). Sebutkan nama, versi, jumlah observasi, jumlah fitur, kelas target, dan lisensi/ketentuan penggunaan.
- Bila memakai dataset publik yang umum (mis. Bank Marketing, Home Credit), sebutkan varian berkasnya (mis. `bank-full.csv`, `bank-additional.csv`) karena nama umum tidak menjamin ukuran dan kolom sama.

## Pra-pemrosesan yang perlu dilaporkan (Bab 3)

- Pembersihan data dan penanganan nilai hilang (missing value).
- Penanganan anomali/pencilan.
- Rekayasa fitur (feature engineering).
- Pembagian data: proporsi train/validation/test, metode (mis. stratified split), dan alasan.
- Penanganan ketidakseimbangan kelas (mis. SMOTE, class weighting) bila ada.
- Normalisasi/standardisasi bila dipakai.

## Reproduksibilitas

- Catat **seed** acak untuk pembagian data dan inisialisasi model.
- Catat **versi** perangkat lunak dan pustaka (mis. Python, scikit-learn, TensorFlow/PyTorch, versi library lain).
- Catat **hyperparameter** dan cara optimasinya (mis. Optuna, grid search) beserta ruang pencarian.
- Simpan **ledger klaim**: setiap angka hasil pada naskah dapat dilacak ke berkas keluaran mentah (nama berkas, skrip, baris/tabel).

## Etika dan integritas data

- Jangan memanipulasi atau merekayasa data agar sesuai harapan (fabrikasi/falsifikasi) [PDF 9 / cetak 8].
- Anonimkan data pribadi bila ada; jangan menyertakan data pribadi sensitif pada lampiran.
- Lampiran kode tidak boleh memuat kredensial, token, atau data pribadi.

## Verifikasi

- Setiap tabel/grafik pada Bab 4 berasal dari eksperimen yang dapat diulang dengan seed dan versi yang dicatat.
- Angka pada naskah sama dengan berkas hasil mentah; perbedaan dibahas, bukan disembunyikan.
- Sumber dan lisensi dataset disebutkan pada Bab 3.
- Bila bagian eksperimen tidak dapat diuji (berkas tidak tersedia), tandai `belum dapat diuji`, jangan menebak.
