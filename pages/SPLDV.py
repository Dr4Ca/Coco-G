import streamlit as st

st.title("SISTEM PERSAMAAN LINEAR DUA VARIABEL")
st.subheader("Persamaan 1: ax+by=c")
a = st.number_input("Masukan Nilai Variabel a")
b = st.number_input("Masukan Nilai Variabel b")
c = st.number_input("Masukan Nilai Variabel c")
st.subheader("Persamaan 2: px+qy=r")
p = st.number_input("Masukan Nilai Variabel p")
q = st.number_input("Masukan Nilai Variabel q")
r = st.number_input("Masukan Nilai Variabel r")

try: #Coba x = blablabla y = blablabla
    x = (c*q-r*b)/(a*q-p*b)
    y = (1/b)*(c-a*x)
except ZeroDivisionError: #Kecuali x = 0 y = 0
    x = 0 #Berarti ngubah semua valuenya jadi 0?
    y = 0
st.caption("Note: AI KAKURU akan mencari variabel x dengan metode eliminasi lalu mencari variabel y dengan metode subtitusi")