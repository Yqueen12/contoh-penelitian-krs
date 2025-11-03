# file: dashboard_app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Judul Dashboard
# ------------------------------
st.set_page_config(page_title="Dashboard Sederhana", layout="wide")
st.title("📊 Dashboard Data Sederhana")

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.header("Filter Data")

# Contoh data
np.random.seed(42)
data = pd.DataFrame({
    'Tanggal': pd.date_range('2025-01-01', periods=100),
    'Kategori': np.random.choice(['A', 'B', 'C'], size=100),
    'Nilai': np.random.randint(50, 150, size=100)
})

# Filter kategori
kategori = st.sidebar.multiselect(
    "Pilih Kategori:",
    options=data['Kategori'].unique(),
    default=data['Kategori'].unique()
)

# Filter data berdasarkan pilihan
filtered_data = data[data['Kategori'].isin(kategori)]

# ------------------------------
# Tampilkan Data
# ------------------------------
st.subheader("📋 Data yang Ditampilkan")
st.dataframe(filtered_data, use_container_width=True)

# ------------------------------
# Statistik Sederhana
# ------------------------------
st.subheader("📈 Statistik Nilai")
col1, col2, col3 = st.columns(3)
col1.metric("Rata-rata", f"{filtered_data['Nilai'].mean():.2f}")
col2.metric("Maksimum", f"{filtered_data['Nilai'].max():.2f}")
col3.metric("Minimum", f"{filtered_data['Nilai'].min():.2f}")

# ------------------------------
# Visualisasi
# ------------------------------
st.subheader("📊 Grafik Nilai per Tanggal")

fig, ax = plt.subplots(figsize=(10, 4))
for k in kategori:
    subset = filtered_data[filtered_data['Kategori'] == k]
    ax.plot(subset['Tanggal'], subset['Nilai'], label=f'Kategori {k}')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Nilai")
ax.legend()
st.pyplot(fig)

st.markdown("---")
st.markdown("💡 *Contoh dashboard sederhana menggunakan Streamlit*")
