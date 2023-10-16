# Polusi Debu Beijing Dashboard
![Polusi Debu Beijing Dashboard](https://github.com/ekasetyo090/air_quality_dashboard/blob/79a836a5066b3fa90525107e79ed06e81933e415/screenshot/tampilan%20penuh.png)

## Daftar isi

- [Deskripsi](#deskripsi)
- [Fitur](#fitur)
- [Instalasi](#instalasi)

## Deskripsi:
Proyek ini adalah pembuatan sebuah dashboard interaktif yang digunakan untuk menganalisis tingkat polusi debu di kota Beijing. Data yang digunakan dalam proyek ini diperoleh dari sumber yang mencatat konsentrasi partikel debu (PM 2.5 & PM 10) di 12 stasiun kota Beijing. Kemudian, proyek mengambil rata-rata konsentrasi (PM 2.5 & PM 10) disetiap jamnya dan menjumlahkan PM 2.5 & PM 10.

Proyek ini memiliki tujuan untuk memberikan wawasan yang lebih baik tentang tingkat polusi debu di Beijing kepada pemangku kepentingan seperti pemerintah, peneliti, dan masyarakat umum. Dengan menggunakan dashboard ini, pengguna dapat memantau perubahan polusi debu selama periode tertentu dan membuat keputusan berdasarkan data yang diberikan.

## Fitur:

### Filter:
#### Rentang Waktu dan Hari:
![Filter](https://github.com/ekasetyo090/air_quality_dashboard/blob/79a836a5066b3fa90525107e79ed06e81933e415/screenshot/fitur%20filter.png)
Memilih rentang waktu visualisasi data, dan pemilihan hari untuk menampilkan konsentrasi debu di waktu tertentu pada hari yang dipilih.

### Visualisasi:

#### Konsentrasi Debu Pada Rentang Waktu Yang Dipilih:
![Konsentrasi Debu Pada Rentang Waktu Yang Dipilih](https://github.com/ekasetyo090/air_quality_dashboard/blob/79a836a5066b3fa90525107e79ed06e81933e415/screenshot/total%20konsentrasi.png)
Menampilkan bagan garis untuk dapat melihat pola konsentrasi debu pada rentang waktu yang dipilih.

#### Konsentrasi Debu Total:
![Konsentrasi Debu Total](https://github.com/ekasetyo090/air_quality_dashboard/blob/79a836a5066b3fa90525107e79ed06e81933e415/screenshot/hari%20paling%20berdebu.png)
Menampilkan bagan total rata-rata konsentrasi debu pada hari tertentu pada rentang waktu yang dipilih.

#### Konsentrasi Debu Waktu Tertentu:
![Konsentrasi Debu Waktu Tertentu](https://github.com/ekasetyo090/air_quality_dashboard/blob/79a836a5066b3fa90525107e79ed06e81933e415/screenshot/konsentrasi%20debu%20di%20waktu%20tertentu.png)
Menampilkan bagan garis untuk dapat melihat pola konsentrasi debu pada waktu tertentu pada hari yang dipilih.

## Instalasi:
#### Setup:
1. git clone https://github.com/ekasetyo090/air_quality_dashboard.git
2. pip install -r requirements.txt

#### Run Streamlit App:
1. streamlit run dashboard.py
