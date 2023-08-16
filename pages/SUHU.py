import streamlit as st

st.title("SUHU")
c = st.number_input("Masukan Nilai Celcius")
st.subheader("KONVERSI")
fahrenheit = (9/5) * c + 32
kelvin = c + 273.15
st.write("Fahrenheit : ", fahrenheit)
st.write("Kelvin : ", kelvin)
