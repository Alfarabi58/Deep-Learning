import eda
import predict
import streamlit as st

navigation = st.sidebar.selectbox('Navigation', ['Exploratory Data Analysis', 'Tweets Sentiment Detection'])

import streamlit as st

# Judul sidebar
st.sidebar.title('Tentang Tweet Covid-19')

# Deskripsi aplikasi
st.sidebar.markdown(
    "Selamat datang di aplikasi analisis Tweet Covid-19! Di sini, Anda dapat menjelajahi berbagai analisis teks "
    "yang dilakukan terhadap tweet terkait Covid-19. Kami mengumpulkan data dari seluruh dunia untuk memahami bagaimana "
    "perasaan, pendapat, dan informasi seputar pandemi ini disebarkan di media sosial."
)

# Fitur aplikasi
st.sidebar.subheader('Fitur Aplikasi:')
st.sidebar.markdown("- **Word Cloud:** Lihat representasi visual dari kata-kata yang paling sering digunakan dalam tweet berdasarkan sentimen (positif, netral, negatif).")
st.sidebar.markdown("- **Analisis Sentimen:** Analisis mendalam tentang bagaimana tweet diklasifikasikan berdasarkan sentimen mereka.")
st.sidebar.markdown("- **Prediksi Sentimen:** Coba prediksi sentimen dari tweet Anda sendiri menggunakan model yang telah dilatih.")

# Panduan penggunaan
st.sidebar.subheader('Panduan Penggunaan:')
st.sidebar.markdown("1. **Unggah Data:** Unggah data tweet Anda sendiri untuk dianalisis.")
st.sidebar.markdown("2. **Eksplorasi Word Cloud:** Jelajahi word cloud berdasarkan sentimen untuk melihat kata-kata kunci yang muncul dalam tweet.")
st.sidebar.markdown("3. **Prediksi Sentimen:** Masukkan teks tweet untuk mendapatkan prediksi sentimen secara real-time.")

# Kontak atau informasi tambahan
st.sidebar.markdown(
    "Kami berharap aplikasi ini membantu Anda dalam memahami dinamika dan tren seputar Covid-19 di media sosial. "
    "Jangan ragu untuk menghubungi kami jika Anda memiliki pertanyaan atau masukan."
)

# Footer atau penutup sidebar
st.sidebar.markdown("**Selamat menjelajah!**")

if navigation == 'Exploratory Data Analysis' :
    eda.run()
else:
    predict.run()