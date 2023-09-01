import streamlit as st

st.title("SISTEM PERSAMAAN LINEAR DUA VARIABEL")

# Function choices
function_choice = st.selectbox("Pilih Fungsi Matematika", ["Diskriminan", "Sumbu Simetri", "Nilai Optimum"])

# Display function explanations
explanations = {
    "Diskriminan": "Diskriminan dari sistem persamaan linear adalah b² - 4ac.",
    "Sumbu Simetri": "Sumbu simetri dari sistem persamaan linear adalah -b/2a.",
    "Nilai Optimum": "Nilai optimum dari sistem persamaan linear adalah -D/4a [-(b² - 4ac)/4a]."
}

st.subheader("Penjelasan:")
st.markdown(explanations[function_choice])

# Function calculations
if function_choice == "Diskriminan":
    db = st.number_input("Masukkan Nilai b", value=0)
    da = st.number_input("Masukkan Nilai a", value=0)
    dc = st.number_input("Masukkan Nilai c", value=0)
    dd = db ** 2 - (4 * da * dc)
    st.subheader(f"Diskriminan adalah: {dd}")

elif function_choice == "Sumbu Simetri":
    xb = st.number_input("Masukkan Nilai b:", value=0)
    xa = st.number_input("Masukkan Nilai a:", value=0)
    x = -xb / (2 * xa)
    st.subheader(f"Sumbu Simetri adalah: {x}")

elif function_choice == "Nilai Optimum":
    nob = st.number_input("Masukkan Nilai b", value=0)
    noa = st.number_input("Masukkan Nilai a", value=0)
    noc = st.number_input("Masukkan Nilai c", value=0)
    nod = (-(nob ** 2 - 4 * noa * noc)) / (4 * noa)
    st.subheader(f"Nilai Optimum adalah: {nod}")

uraian = st.checkbox("Tampilkan hasil uraian")

if uraian:
    if function_choice == "Diskriminan":
        hasil = dd
        st.subheader("Uraian Diskriminan")
        st.write("Untuk menghitung diskriminan, maka menggunakan format (b² - 4ac)")