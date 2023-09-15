import streamlit as st

st.set_page_config(
    page_title="COCO GENIUS",
    page_icon=":tada:",
    layout="wide"
    )

st.sidebar.success("👆SILAHKAN PILIH👆")

st.title("COCO GENIUS")
st.markdown("""
    Orang yang terlibat :
    - Azzam Putra Raihan
    - Raya Zuvla Naila
    - Miftah Putri Ferdani
    - Keira Khumaira Putri Tamrizal
    - M. Delpiero
    - M. Afik
    - Rafikah Ilham
    ### SMA PERMATA INSANI ISLAMIC SCHOOL
    """)

st.image('https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.permatainsaniislamicschool.sch.id%2Fgallery_gen%2F438b7df017e009e8be6fa7a9adbf874e_654x372.984375.png&tbnid=vm8xc83LebQ6YM&vet=12ahUKEwj_5uu02quBAxWd2zgGHcE_CpoQMygAegQIARBX..i&imgrefurl=https%3A%2F%2Fwww.permatainsaniislamicschool.sch.id%2F&docid=L3VHsomLwPogtM&w=654&h=371&q=logo%20permata%20insani%20islamic%20school&ved=2ahUKEwj_5uu02quBAxWd2zgGHcE_CpoQMygAegQIARBX')

st.subheader(":mailbox: Gak nemu rumus? Bilang aja!")
st.write("Website ini masih sepenuhnya dalam pengembangan, jika ada bug atau kesalahan, bisa kontak developer lewat form dibawah👇")

contact_form = """
<form action="https://formsubmit.co/0e4a07a9d07e5a315c5cb8aaae8d758c" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Nama Kamu" required>
     <input type="email" name="email" placeholder="Email Kamu" required>
     <textarea name="message" placeholder="Pesan kamu disini! (Bisa berupa saran atau error!)"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")