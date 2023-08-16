import streamlit as st

st.title("SEGITIGA SAMA KAKI")
st.header("KELILING")
s1 = st.number_input("Masukan Panjang Sisi 1:")
s2 = st.number_input("Masukan Panjang Sisi 2:")
s3 = st.number_input("Masukan Panjang Sisi 3:")
k = s1 + s2 + s3
st.subheader(k)

st.header("LUAS")
a = st.number_input("Masukan Nilai Alas:")
t = st.number_input("Masukan Nilai Tinggi:")
l = 1 / 2 * a * t
st.subheader(l)