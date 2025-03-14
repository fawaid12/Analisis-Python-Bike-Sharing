import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memuat data dari file
file_day = "day.csv"  # Ganti dengan path yang sesuai
file_hour = "hour.csv"  # Ganti dengan path yang sesuai
day = pd.read_csv(file_day)
hour = pd.read_csv(file_hour)

# Mengonversi tanggal ke format datetime
day["dteday"] = pd.to_datetime(day["dteday"])
hour["dteday"] = pd.to_datetime(hour["dteday"])

# Extract year and month
hour['year'] = hour['dteday'].dt.year
hour['month'] = hour['dteday'].dt.month
day['year'] = day['dteday'].dt.year
day['month'] = day['dteday'].dt.month

# Dashboard menggunakan Streamlit
st.title("Dashboard Penyewaan Sepeda")

# Sidebar filters
st.sidebar.header("🔍 Pilih Tahun")
selected_years = st.sidebar.multiselect("Pilih Tahun (Maksimal 2 Tahun)", options=sorted(hour['year'].unique()), default=[hour['year'].min()])

# Filter data berdasarkan tahun
filter_day = day[day['year'].isin(selected_years)]
filter_hour = hour[hour['year'].isin(selected_years)]

# Grafik Penyewaan Sepeda per Jam
st.subheader("Total Penyewa per Jam berdasarkan Tahun")
plt.figure(figsize=(12, 6))
for year in selected_years:
    yearly_hourly_rentals = filter_hour[filter_hour['year'] == year].groupby(['hr'])['cnt'].sum().reset_index()
    plt.plot(yearly_hourly_rentals['hr'], yearly_hourly_rentals['cnt'], marker='o', label=f'tahun {year}')
plt.title('Total Penyewa Sepeda per Jam')
plt.xlabel('jam')
plt.ylabel('jumlah Penyewa')
plt.legend()
st.pyplot(plt)

# Hubungan Bulan dengan Cuaca berdasarkan Jumlah Penyewa Sepeda
st.subheader("Hubungan Bulan dengan Cuaca dan Jumlah Penyewa Sepeda")
weath_month = filter_day.groupby(["mnth", "weathersit"])["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=weath_month["mnth"], y=weath_month["cnt"], hue=weath_month["weathersit"],data=filter_day, palette="crest", ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Hubungan Bulan dengan Cuaca dan Jumlah Penyewa Sepeda")
st.pyplot(fig)

# Hubungan Cuaca dengan Hari berdasarkan Penyewaan Sepeda
st.subheader("Hubungan Cuaca dengan Hari dan Jumlah Penyewa Sepeda")
weath_day = filter_day.groupby(["weekday", "weathersit"])["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=weath_day['weathersit'], y=weath_day['cnt'], hue=weath_day['weekday'], data=filter_day, palette='viridis', ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Hubungan Cuaca dengan Hari dan Jumlah Penyewa Sepeda")
plt.legend(title='Hari Per Minggu', labels=['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
st.pyplot(fig)

# Menampilkan Dataframe yang difilter
st.subheader("Data Penyewaan Sepeda yang Difilter")
st.dataframe(filter_hour)

# Menampilkan total penyewaan sepeda berdasarkan filter yang dipilih
total_penyewaan = filter_hour["cnt"].sum()
st.subheader(f"Total Penyewaan Sepeda: {total_penyewaan}")

# Menampilkan total penyewaan sepeda berdasarkan kondisi cuaca
st.subheader("Total Penyewaan Sepeda Berdasarkan Cuaca")
total_per_cuaca = filter_hour.groupby("weathersit")["cnt"].sum().reset_index()
st.dataframe(total_per_cuaca)
