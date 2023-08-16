import streamlit as st

st.title("PERSAMAAN FUNGSI KUADRAT")
st.header("DISKRIMINAN")
st.subheader("Format: (b² -4 a c)")

db = st.number_input("Masukan Nilai b", value=0)
da = st.number_input("Masukan Nilai a", value=0)
dc = st.number_input("Masukan Nilai c", value=0)

dd = -db**2 - (4 * (da * dc))  # Correction
st.subheader(dd)

st.header("SUMBU SIMETRI")
st.subheader("Format: -b/2a")
xb = st.number_input("Masukan Nilai b:")
xa = st.number_input("Masukan Nilai a:")

try:
    x = -xb / (2 * xa)
except ZeroDivisionError:
    x = 0
st.subheader(x)

st.header("NILAI OPTIMUM")
st.subheader("Format: -D/4a [-(b² - 4ac/4a)]")
nob = st.number_input("Masukan Nilai b ")
noa = st.number_input("Masukan Nilai a ")
noc = st.number_input("Masukan Nilai c ")

try:
    nod = (-(nob**2 -4 * noa * noc)) / (4 * noa)
except ZeroDivisionError:
    nod = 0
st.subheader(nod)