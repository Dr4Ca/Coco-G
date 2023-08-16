import streamlit as st

st.title("ROTASI")
#st.title("SEDANG DALAM PERBAIKAN")
x = st.number_input("Masukan Nilai x")
y = st.number_input("Masukan Nilai y")
st.header("(+90/-270)")
x1 = (-y)
y1 = (x)
st.write('sumbu x:',x1,' sumbu y:', y1)
st.header("(180)")
x2 = (y)
y2 = (-x)
st.write('sumbu x:',x2,' sumbu y:', y2)
st.header("(-90/+270)")
x3 = (-x)
y3 = (-y)
st.write('sumbu x:',x3,' sumbu y:', y3)
#rotasi = st.selectbox(
    #'Masukan jenis Rotasi',
    #('(+90/-270)', '(-90/+270)', '(180)'
    #))
#if +90/-270:
    #x1 = (-y)
    #y1 = (x)
    #st.write('sumbu x:',x1,' sumbu y:', y1)
#else:
    #-90/+270
    #x2 = (y)
    #y2 = (-x)
    #st.write("sumbu x", x2," sumbu y: ", y2)
    #180
    #x3 = (-x)
    #y3 = (-y)
    #st.write('sumbu x:',x3,'sumbu y:', y3)