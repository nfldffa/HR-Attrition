# Submission Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

### Latar Belakang
PT Jaya Jaya Maju menghadapi tantangan dalam mempertahankan talenta terbaiknya. Attrition yang tinggi berdampak pada biaya operasional dan stabilitas tim. Proyek ini menggunakan pendekatan Data Science untuk mengidentifikasi pemicu utama karyawan resign dan menyediakan alat bantu keputusan bagi tim HR.

### Permasalahan Bisnis
1. Apakah lembur (Overtime) menjadi pemicu utama karyawan meninggalkan perusahaan?
2. Bagaimana pengaruh kompensasi (gaji bulanan) terhadap loyalitas karyawan?
3. Apakah lingkungan kerja yang buruk berkolerasi langsung dengan tingkat attrition?
4. Jabatan dan Departemen mana yang memiliki risiko paling kritis?
5. Bagaimana karakteristik karyawan yang berisiko resign agar dapat dilakukan intervensi dini?

### Cakupan Proyek
1. **Data Preparation**: Membersihkan data dan melakukan feature engineering (seperti kategorisasi lembur dan label kepuasan).
2. **Modeling**: Membangun model prediksi menggunakan XGBoost untuk mendeteksi risiko attrition.
3. **Business Dashboard**: Membuat visualisasi interaktif di Looker Studio yang fokus pada perbandingan segmen (bukan sekadar tabel).
4. **Actionable Insights**: Memberikan rekomendasi strategis berdasarkan temuan data.

---

## Business Dashboard

Dashboard ini dirancang secara komprehensif untuk menyajikan analisis faktor pemicu attrition secara cepat dan tepat.

🔗 **Link Dashboard:** [DASHBOARD ANALISIS ATTRITION KARYAWAN - JAYA JAYA MAJU](https://datastudio.google.com/reporting/43f481f8-23f6-4c57-8358-f2da76127c90)

### Komponen Visualisasi Utama:
1. **Summary Scorecards**: Memantau Total Karyawan, Jumlah Resign, dan Attrition Rate secara real-time.
2. **Pengaruh Lembur (Overtime)**: Visualisasi 100% Stacked Bar yang menunjukkan porsi resign yang signifikan pada karyawan yang sering lembur.
3. **Analisis Segmen Departemen**: Donut Chart yang membandingkan kontribusi attrition dari tiap departemen (Sales, R&D, HR).
4. **Top Attrition by Job Role**: Bar Chart Horizontal yang mengurutkan jabatan dengan tingkat resign tertinggi (Laboratory Technician, Sales Representative, dsb).
5. **Korelasi Gaji Bulanan**: Perbandingan rata-rata gaji antara karyawan yang bertahan vs yang resign untuk melihat pengaruh kompensasi.
6. **Analisis Lingkungan Kerja**: Grafik kepuasan lingkungan kerja (skala 1-4) yang membuktikan bahwa lingkungan yang buruk meningkatkan risiko attrition.

---

## Conclusion & Insights

### Kesimpulan Analisis:
* **Overtime adalah Red Flag**: Karyawan yang lembur memiliki persentase resign yang jauh lebih tinggi. Ini adalah faktor pemicu nomor satu.
* **Kesenjangan Kompensasi**: Rata-rata gaji karyawan yang resign lebih rendah dibandingkan mereka yang bertahan, mengindikasikan adanya isu daya saing gaji.
* **Faktor Psikologis**: Tingkat kepuasan lingkungan (Environment Satisfaction) berbanding terbalik dengan angka attrition. Semakin rendah kepuasan, semakin besar kemungkinan karyawan keluar.
* **Departemen Kritis**: Departemen Sales dan R&D memerlukan perhatian khusus karena memiliki volume attrition tertinggi.

### Rekomendasi Action Items:
1. **Evaluasi Beban Kerja**: Meninjau ulang kebijakan lembur dan mendistribusikan beban kerja secara lebih merata atau memberikan insentif lembur yang lebih menarik.
2. **Review Kompensasi**: Melakukan benchmarking gaji secara berkala, terutama untuk posisi teknis seperti Laboratory Technician agar tidak kalah saing dengan pasar.
3. **Perbaikan Fasilitas & Kultur**: Melakukan intervensi pada tim dengan tingkat kepuasan lingkungan rendah melalui perbaikan fasilitas kantor atau program team-building.
4. **Intervensi Dini**: Menggunakan model prediksi untuk mendekati karyawan berisiko tinggi (High Risk) sebelum mereka mengajukan surat resign.

---

## Cara Menjalankan Prediksi (Model)
Script `prediction.py` telah disediakan untuk melakukan prediksi secara interaktif.
1. Install requirements: `pip install -r requirements.txt`
2. Jalankan script: `python prediction.py`
3. Masukkan data karyawan saat diminta di terminal untuk melihat status prediksi (Stay/Resign).