import streamlit as st

def hitung_keliling(r, use_approximation):
    if use_approximation and r % 7 == 0:
        pi = 22/7
    else:
        pi = 3.14
    keliling = 2 * pi * r
    return keliling

def hitung_luas(r, use_approximation):
    if use_approximation and r % 7 == 0:
        pi = 22/7
    else:
        pi = 3.14
    luas = 4 * pi * r * r
    return luas

def hitung_volume(r, use_approximation):
    if use_approximation and r % 7 == 0:
        pi = 22/7
    else:
        pi = 3.14
    volume = (4/3) * pi * r * r * r
    return volume

def main():
    st.title("Bola")
    r = st.number_input("Masukkan jari-jari bola:", min_value=0.0)
    
    # Dropdown untuk memilih operasi
    selected_operation = st.selectbox("Pilih operasi:", ["Keliling", "Luas Permukaan", "Volume"])
    
    # Checkbox untuk kelipatan 7
    use_approximation = st.checkbox("Gunakan 22/7 jika jari-jari adalah kelipatan 7", value=(r % 7 == 0))
    
    if selected_operation == "Keliling":
        hasil = hitung_keliling(r, use_approximation)
        st.subheader("Hasil Keliling:")
        st.write(hasil)
    elif selected_operation == "Luas Permukaan":
        hasil = hitung_luas(r, use_approximation)
        st.subheader("Hasil Luas Permukaan:")
        st.write(hasil)
    else:
        hasil = hitung_volume(r, use_approximation)
        st.subheader("Hasil Volume:")
        st.write(hasil)

if __name__ == "__main__":
    main()
