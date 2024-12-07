# Sistem Deteksi Pesan Penipuan Naive Bayes

Program ini merupakan sistem deteksi pesan penipuan menggunakan algoritma Naive Bayes. Sistem ini telah diuji dan mendapatkan akurasi model sebesar 92.14%.

## Cara Kerja

Sistem ini bekerja dengan cara berikut:

1. **Preprocessing:** Pesan teks yang masuk akan diproses terlebih dahulu untuk membersihkan dan menormalisasi teks. Tahapan ini meliputi case folding, normalisasi teks, filtering (stopword removal), dan stemming.
2. **Feature Extraction:** Setelah diproses, pesan teks akan diekstrak fiturnya menggunakan metode **TF-IDF (Term Frequency-Inverse Document Frequency)**. Metode ini menghitung bobot setiap kata dalam pesan teks berdasarkan frekuensi kemunculannya dalam pesan tersebut dan dalam seluruh dataset. 
3. **Feature Selection:** Fitur yang telah diekstrak akan diseleksi untuk mendapatkan fitur yang paling relevan menggunakan metode **Chi-Square**. Metode ini akan memilih fitur-fitur yang memiliki korelasi yang kuat dengan label kelas (penipuan atau bukan penipuan).
4. **Modeling:** Model **Naive Bayes** akan dilatih menggunakan data yang telah diproses dan diseleksi fiturnya. Algoritma Naive Bayes merupakan algoritma klasifikasi probabilistik yang sederhana namun efektif, yang bekerja berdasarkan teorema Bayes.
5. **Prediksi:** Pesan teks baru yang masuk akan diprediksi oleh model untuk menentukan apakah pesan tersebut merupakan pesan penipuan atau bukan.

## Akurasi Model

Sistem ini telah diuji dan mendapatkan akurasi model sebesar 92.14%. Hal ini menunjukkan bahwa sistem ini cukup akurat dalam mendeteksi pesan penipuan.

## Penggunaan

Untuk menggunakan sistem ini, Anda dapat mengikuti langkah-langkah berikut:

1. Unduh kode program dari repositori ini.
2. Pasang library yang dibutuhkan.
3. Jalankan program.
4. link website https://sistem-deteksi-pesan-penipuan.streamlit.app/
