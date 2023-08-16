import streamlit as st

st.title("PERSEGI")

selected_operation = st.selectbox("Pilih Operasi:", ['Keliling', 'Luas'])

if selected_operation == "Keliling":
    sisi = st.number_input("Masukan Nilai sisi:")
    

#st.header("KELILING")
#keliling = sisi**2
#st.subheader(keliling)

#st.header("LUAS")
#luas = 4 * sisi
#st.subheader(luas)