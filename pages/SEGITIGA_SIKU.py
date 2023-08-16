import streamlit as st

st.title("SEGITIGA SIKU-SIKU")

#Mencari Keliling
st.header("KELILING")
a = st.number_input("Masukan Panjang sisi 1")
b = st.number_input("Masukan Panjang sisi 2")
c = st.number_input("Masukan Panjang sisi 3")
k = a + b + c
st.subheader(k)
#Mencari Luas
st.header("LUAS")
alas = st.number_input("Masukan panjang Alas")
tinggi = st.number_input("Masukan Tinggi")
l = alas * tinggi * 1 / 2
st.subheader(l)
#Mencari Alas
st.header("MENCARI ALAS")
kll = st.number_input("Masukan Keliling:")
als = kll / 3
st.subheader(als)

#Mencari tinggi
st.header("MENCARI TINGGI")
ls = st.number_input("Masukan Nilai luas")
t = ls * 1 / 2
st.header(t)
