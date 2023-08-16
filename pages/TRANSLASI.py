import streamlit as st

st.title("TRANSLASI")
st.header("MENCARI TITIK AWAL")
xxi = st.number_input("Masukan Nilai X1")
yyi = st.number_input("Masukan Nilai Y1")
xxa = st.number_input("Masukan Nilai a")
yyb = st.number_input("Masukan Nilai b")
x = xxi - xxa
y = yyi - yyb
st.write("(",x, ",",y,")")

st.header("MENCARI TITIK TRANSLASI")
ax1 = st.number_input("Masukan Nilai X1 ")
by1 = st.number_input("Masukan Nilai Y1 ")
ax = st.number_input("Masukan Nilai X")
ay = st.number_input("Masukan Nilai Y")
a = ax1 - ax
b = by1 - ay
st.write("(", a,",",b,")")

st.header("MENCARI TITIK BAYANGAN")
x1a = st.number_input("Masukan Nilai a ")
y1b = st.number_input("Masukan Nilai b ")
x1x = st.number_input("Masukan Nilai x ")
x1y = st.number_input("Masukan Nilai y ")
x1 = x1a + x1x
y1 = y1b + x1y
st.write("(", x1,",",y1,")")
