import streamlit as st

st.title("KUBUS")
st.header("KELILING, LUAS, DAN VOLUME")

sop = st.selectbox("Pilih operasi:", ["Keliling", "Luas", "Volume"])

sisi = st.number_input("Masukan Nilai Panjang:")
if sop == "Keliling":
    hasil = 12 * sisi
    st.subheader(hasil)
elif sop == "Luas":
    hasil = 6 * sisi
    st.subheader(hasil)
elif sop == "Volume":
    hasil = sisi * sisi * sisi
    st.subheader(hasil)

uraian = st.checkbox("Tampilkan hasil uraian")

if uraian:
    if sop == "Keliling":
        hasil = 12 * sisi
        st.subheader("Uraian Keliling:")
        st.write(f"Untuk menghitung keliling kubus, diketahui = {sisi}")
        st.write("Rumus keliling adalah 12 * sisi")
        st.write(f"Jadi, hasil keliling kubus = 12 * {sisi} = {hasil}.")
    elif sop == "Luas":
        hasil = 6 * sisi
        st.subheader("Uraian Luas:")
        st.write(f"Untuk menghitung luas kubus, diketahui = {sisi}")
        st.write("Rumus luas adalah 6 * sisi")
        st.write(f"Jadi, hasil luas kubus = 6 * {sisi} = {hasil}.")
    elif sop == "Keliling":
        hasil = sisi * sisi * sisi
        st.subheader("Uraian Volume:")
        st.write(f"Untuk menghitung volum kubus, diketahui = {sisi}")
        st.write("Rumus volum adalah sisi * sisi * sisi")
        st.write(f"Jadi, hasil keliling kubus = {sisi}**3 = {hasil}.")
