import streamlit as st

st.title("BANGUN RUANG BALOK")
st.header("KELILING, LUAS, DAN VOLUME")

# Dropdown untuk memilih operasi
selected_operation = st.selectbox("Pilih operasi:", ["Keliling", "Luas Permukaan", "Volume"])

# Input nilai panjang, lebar, dan tinggi
p = st.number_input("Masukkan Nilai Panjang:")
l = st.number_input("Masukkan Nilai Lebar:")
t = st.number_input("Masukkan Nilai Tinggi:")

# Menampilkan uraian hasil
uraian_shown = st.checkbox("Tampilkan hasil uraian")

if uraian_shown:
    if selected_operation == "Keliling":
        hasil = 4 * (p + l + t)
        st.subheader("Uraian Keliling:")
        st.write(f"Untuk menghitung keliling balok, diketahui panjang = {p}, lebar = {l}, dan tinggi = {t}.")
        st.write("Rumus keliling adalah 4 * (panjang + lebar + tinggi).")
        st.write(f"Jadi, hasil keliling balok = 4 * ({p} + {l} + {t}) = {hasil}.")
    elif selected_operation == "Luas Permukaan":
        hasil = (p * l) + (p * t) + (l * t)
        st.subheader("Uraian Luas Permukaan:")
        st.write(f"Untuk menghitung luas permukaan balok, diketahui panjang = {p}, lebar = {l}, dan tinggi = {t}.")
        st.write("Rumus luas permukaan adalah panjang * lebar + panjang * tinggi + lebar * tinggi.")
        st.write(f"Jadi, hasil luas permukaan balok = ({p} * {l}) + ({p} * {t}) + ({l} * {t}) = {hasil}.")
    else:
        hasil = p * l * t
        st.subheader("Uraian Volume:")
        st.write(f"Untuk menghitung volume balok, diketahui panjang = {p}, lebar = {l}, dan tinggi = {t}.")
        st.write("Rumus volume adalah panjang * lebar * tinggi.")
        st.write(f"Jadi, hasil volume balok = {p} * {l} * {t} = {hasil}.")

# Menampilkan hasil perhitungan sesuai operasi yang dipilih
if selected_operation == "Keliling":
    hasil = 4 * (p + l + t)
    st.subheader("Hasil Keliling:")
    st.write(hasil)
elif selected_operation == "Luas Permukaan":
    hasil = (p * l) + (p * t) + (l * t)
    st.subheader("Hasil Luas Permukaan:")
    st.write(hasil)
else:
    hasil = p * l * t
    st.subheader("Hasil Volume:")
    st.write(hasil)
