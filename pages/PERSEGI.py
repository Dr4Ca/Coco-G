import streamlit as st

st.title("PERSEGI")

selected_operation = st.selectbox("Pilih Operasi:", ['Keliling', 'Luas'])

if selected_operation == "Keliling":
    sisi = st.number_input("Masukan Nilai sisi:")
    keliling = sisi**2
    st.subheader(keliling)
elif selected_operation == "Luas":
    sisi = st.humber_input("Masukan Nilai sisi:")
    luas = 4 * sisi
    st.subheader(luas)