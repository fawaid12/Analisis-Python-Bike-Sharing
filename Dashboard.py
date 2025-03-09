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

# Dashboard menggunakan Streamlit
st.title("Dashboard Penyewaan Sepeda")

# Filter berdasarkan rentang tanggal, rentang waktu, dan cuaca
date_range = st.date_input("Pilih Rentang Tanggal", [day["dteday"].min(), day["dteday"].max()], min_value=day["dteday"].min(), max_value=day["dteday"].max())
time_range = st.slider("Pilih Rentang Waktu", 0, 23, (6, 18))
cuaca_options = ["Semua Cuaca"] + sorted(hour["weathersit"].unique().tolist())
cuaca = st.multiselect("Pilih Kondisi Cuaca", options=cuaca_options, default="Semua Cuaca")

# Filter data
filter_day = day[(day["dteday"] >= pd.to_datetime(date_range[0])) & (day["dteday"] <= pd.to_datetime(date_range[1]))]
if "Semua Cuaca" in cuaca:
    filter_hour = hour[(hour["dteday"] >= pd.to_datetime(date_range[0])) & (hour["dteday"] <= pd.to_datetime(date_range[1])) & (hour["hr"] >= time_range[0]) & (hour["hr"] <= time_range[1])]
else:
    filter_hour = hour[(hour["dteday"] >= pd.to_datetime(date_range[0])) & (hour["dteday"] <= pd.to_datetime(date_range[1])) & (hour["hr"] >= time_range[0]) & (hour["hr"] <= time_range[1]) & (hour["weathersit"].isin(cuaca))]

# Grafik Penyewaan Sepeda Harian
st.subheader("Total Penyewaan Sepeda per Hari")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(filter_day["dteday"].dt.strftime('%Y-%m-%d'), filter_day["cnt"], color='skyblue', edgecolor='black')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Total Penyewaan Sepeda per Hari")
plt.xticks(rotation=45)
st.pyplot(fig)

# Grafik Penyewaan Sepeda per Jam
st.subheader("Penyewaan Sepeda berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(filter_hour["hr"], filter_hour["cnt"], color='green', edgecolor='black')
ax.set_xlabel("Jam")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Penyewaan Sepeda berdasarkan Jam")
st.pyplot(fig)

# Hubungan Bulan dengan Cuaca berdasarkan Jumlah Penyewa Sepeda
st.subheader("Hubungan Bulan dengan Cuaca dan Jumlah Penyewa Sepeda")
weath_month = filter_day.groupby(["mnth", "weathersit"])["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=weath_month["mnth"], y=weath_month["cnt"], hue=weath_month["weathersit"], palette="coolwarm", ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Hubungan Bulan dengan Cuaca dan Jumlah Penyewa Sepeda")
st.pyplot(fig)

# Hubungan Cuaca dengan Hari berdasarkan Penyewaan Sepeda
st.subheader("Hubungan Cuaca dengan Hari dan Jumlah Penyewa Sepeda")
weath_day = filter_day.groupby(["dteday", "weathersit"])["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=weath_day["dteday"], y=weath_day["cnt"], hue=weath_day["weathersit"], palette="coolwarm", ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Hubungan Cuaca dengan Hari dan Jumlah Penyewa Sepeda")
plt.xticks(rotation=45)
st.pyplot(fig)

# Menampilkan Dataframe yang difilter
st.subheader("Data Penyewaan Sepeda yang Difilter")
st.dataframe(filter_hour)

# Menampilkan total penyewaan sepeda berdasarkan filter yang dipilih
total_penyewaan = filter_hour["cnt"].sum()
st.subheader(f"Total Penyewaan Sepeda: {total_penyewaan}")

# Menampilkan total penyewaan sepeda berdasarkan kondisi cuaca
st.subheader("Total Penyewaan Sepeda Berdasarkan Cuaca")
df_total_per_cuaca = filter_hour.groupby("weathersit")["cnt"].sum().reset_index()
st.dataframe(df_total_per_cuaca)
