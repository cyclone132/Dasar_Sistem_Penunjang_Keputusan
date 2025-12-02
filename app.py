import streamlit as st
import pandas as pd

# ----------------------
# Inisialisasi Data
# ----------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Kategori", "Nilai"])

st.title("📊 Aplikasi Analisis Data Sederhana (Streamlit)")

st.write("Masukkan data secara manual, lalu lihat tabel dan grafik analisisnya.")

# ----------------------
# Form Input
# ----------------------
with st.form("input_form"):
    kategori = st.text_input("Kategori (contoh: Produk A, Produk B, dll.)")
    nilai = st.number_input("Nilai", min_value=0, step=1)
    submitted = st.form_submit_button("Tambah Data")

# Tambahkan data ke dataframe session state
if submitted:
    if kategori.strip() == "":
        st.warning("Kategori tidak boleh kosong!")
    else:
        st.session_state.data.loc[len(st.session_state.data)] = [kategori, nilai]
        st.success("Data berhasil ditambahkan!")

# ----------------------
# Tampilkan Tabel Data
# ----------------------
st.subheader("📋 Tabel Data")
st.dataframe(st.session_state.data)

# ----------------------
# Grafik Analisis Data
# ----------------------
if not st.session_state.data.empty:
    st.subheader("📈 Grafik Analisis")

    # Bar Chart
    st.write("### Bar Chart")
    st.bar_chart(st.session_state.data.set_index("Kategori"))

    # Line Chart
    st.write("### Line Chart")
    st.line_chart(st.session_state.data.set_index("Kategori"))

    # Pie Chart (Plotly)
    import plotly.express as px
    st.write("### Pie Chart")
    fig = px.pie(
        st.session_state.data,
        names="Kategori",
        values="Nilai",
        title="Distribusi Nilai per Kategori"
    )
    st.plotly_chart(fig)

else:
    st.info("Masukkan data terlebih dahulu untuk menampilkan grafik.")