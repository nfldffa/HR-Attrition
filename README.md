# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
PT Jaya Jaya Maju saat ini sedang menghadapi tantangan dalam mempertahankan talenta terbaiknya. Tingginya angka pengunduran diri karyawan (attrition) berdampak pada meningkatnya biaya operasional rekrutmen serta gangguan pada stabilitas produktivitas tim. Proyek ini bertujuan untuk mengidentifikasi faktor-faktor kunci penyebab attrition agar manajemen dapat mengambil kebijakan retensi yang lebih efektif dan tepat sasaran.

### Permasalahan Bisnis
1. Apakah kebijakan lembur (Overtime) memiliki korelasi kuat terhadap keputusan resign karyawan?
2. Bagaimana pengaruh tingkat kompensasi (Monthly Income) terhadap loyalitas karyawan di perusahaan?
3. Apakah rendahnya kualitas lingkungan kerja (Environment Satisfaction) menjadi pendorong utama attrition?
4. Jabatan (Job Role) dan Departemen mana yang memiliki risiko attrition paling kritis?
5. Bagaimana cara memprediksi karyawan yang berisiko resign agar tim HR dapat melakukan intervensi dini?

### Cakupan Proyek
1. **Data Cleaning & Preparation**: Melakukan pembersihan data, penanganan missing values, dan transformasi fitur agar siap digunakan untuk analisis.
2. **Exploratory Data Analysis (EDA)**: Menemukan pola dan korelasi antara variabel (seperti Gaji, Lembur, dan Kepuasan) terhadap status attrition.
3. **Machine Learning Modeling**: Mengembangkan model klasifikasi menggunakan algoritma XGBoost untuk memprediksi probabilitas karyawan akan keluar dari perusahaan.
4. **Business Dashboard Development**: Membangun dashboard interaktif di Looker Studio untuk memonitor metrik attrition secara real-time.

### Persiapan
**Sumber data:** [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

**Versi Python:** `Python 3.11`

**Setup Environment:**

1. **Membuat Virtual Environment:**
   Buka terminal atau command prompt pada direktori proyek, lalu jalankan perintah berikut:
   ```bash
   python -m venv venv
   ```

2. **Mengaktifkan Virtual Environment:**
   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\activate
     ```
   - **macOS/Linux (Bash):**
     ```bash
     source venv/bin/activate
     ```

3. **Instalasi Dependency:**
   Gunakan file `requirements.txt` untuk menginstal semua library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

4. **Menjalankan Script Prediksi:**
   Untuk menjalankan proses prediksi attrition secara interaktif menggunakan script `.py`, gunakan perintah:
   ```bash
   python prediction.py
   ```

---

## Business Dashboard
Dashboard ini dirancang secara komprehensif untuk menyajikan analisis faktor pemicu attrition secara cepat dan tepat melalui Looker Studio.

🔗 **Link Dashboard:** [DASHBOARD ANALISIS ATTRITION KARYAWAN](https://datastudio.google.com/u/0/reporting/43f481f8-23f6-4c57-8358-f2da76127c90/page/NKjvF)

### Komponen Visualisasi Utama:
1. **Summary Scorecards**: Memantau Total Karyawan, Jumlah Resign, dan Attrition Rate secara real-time.
2. **Pengaruh Lembur (Overtime)**: Visualisasi porsi resign yang signifikan pada karyawan yang memiliki riwayat lembur.
3. **Analisis Segmen Departemen**: Perbandingan kontribusi attrition dari tiap departemen (Sales, R&D, HR).
4. **Top Attrition by Job Role**: Mengurutkan jabatan dengan tingkat resign tertinggi (Laboratory Technician, Sales Representative, dsb).
5. **Korelasi Finansial**: Perbandingan rata-rata gaji antara karyawan yang bertahan vs yang resign.

---

## Conclusion
Berdasarkan hasil analisis dan pemodelan data, dapat ditarik beberapa kesimpulan utama:
- **Kebijakan Lembur (Overtime):** Karyawan yang sering bekerja lembur memiliki tingkat attrition yang jauh lebih tinggi.
- **Kompensasi Finansial:** Rata-rata gaji bulanan (Monthly Income) karyawan yang resign cenderung lebih rendah dibandingkan mereka yang bertahan.
- **Kepuasan Lingkungan:** Karyawan dengan rating kepuasan lingkungan kerja yang rendah menunjukkan kecenderungan resign yang lebih besar.
- **Segmen Berisiko:** Jabatan teknis seperti Laboratory Technician dan posisi penjualan seperti Sales Representative menunjukkan angka attrition tertinggi.

### Rekomendasi Action Items
* **Evaluasi Kebijakan Lembur:** Mengkaji ulang distribusi beban kerja untuk meminimalkan burnout.
* **Review Struktur Gaji:** Melakukan benchmarking kompensasi agar tetap kompetitif di pasar.
* **Peningkatan Engagement:** Memperbaiki fasilitas dan kultur kerja pada departemen dengan skor kepuasan rendah.
* **Intervensi Berbasis Data:** Menggunakan model prediksi untuk mendeteksi karyawan "High Risk" secara preventif.