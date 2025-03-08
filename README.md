# Analisis-Python-Bike-Sharing
Analisis data bike sharing dan dashboard visualisasi data


## Deskripsi
Dashboard ini dibuat menggunakan Streamlit untuk menganalisis data penyewaan sepeda berdasarkan berbagai filter seperti rentang waktu, kondisi cuaca, dan tanggal tertentu.

## Fitur
- **Filter Interaktif**: Memungkinkan pengguna untuk memfilter data berdasarkan tanggal, jam, dan kondisi cuaca.
- **Visualisasi Data**: Grafik penyewaan sepeda per hari, per jam, hubungan bulan dengan cuaca, dan hubungan cuaca dengan hari.
- **Total Penyewaan**: Menampilkan total penyewaan sepeda berdasarkan filter yang dipilih.

## Instalasi
1. Pastikan Python telah terinstall di sistem Anda.
2. Install dependensi menggunakan perintah berikut:
   ```sh
   pip install -r requirements.txt
   ```

## Menjalankan Dashboard
Jalankan perintah berikut di terminal atau command prompt:
```sh
streamlit run dashboard.py
```

## Struktur File
```
|-- day.csv             # Dataset harian
|-- hour.csv            # Dataset per jam
|-- Dashboard.py        # File utama untuk menjalankan dashboard
|-- analisis.ipynb      # File ipynb dijupiter untuk langkah-langkah analisis
|-- requirements.txt    # Daftar dependensi
|-- README.md           # Dokumentasi proyek
|-- url.txt             # link streamlit
```

## Dataset
Dataset yang digunakan berasal dari file `day.csv` dan `hour.csv`, yang berisi informasi tentang penyewaan sepeda berdasarkan waktu dan kondisi cuaca.

## Kontributor
- **Muhammad Fawaid As'ad**
