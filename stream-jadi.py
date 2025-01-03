import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

#load save model
model_fraud = pickle.load(open('model_fraud.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf_idf.sav", "rb"))))

# st.image('logo.webp', width=200)

st.markdown("""
Selamat datang di aplikasi prediksi pesan penipuan! Masukkan pesan Anda di bawah untuk mendeteksi apakah pesan tersebut adalah pesan fraud, normal, atau promo.
""")


# judul halaman
st.title ('Prediksi Pesan Penipuan')

clean_teks = st.text_input('Masukkan Text Pesan')

fraud_detection = ''

if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))

    if (predict_fraud == 0):
        fraud_detection = 'PESAN Normal'
    elif (predict_fraud == 1):
        fraud_detection = 'PESAN Fraud'
    else :
        fraud_detection = 'PESAN Promo'
    
    st.success(fraud_detection)
    
