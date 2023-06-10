import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Data Mining  Prediksi Diabetes')

Pregnancies	= st.text_input ('input nilai Pregnancies')

Glucose = st.text_input ('input nilai Glucose')

BloodPressure = st.text_input ('input nilai BloodPressure')

SkinThickness = st.text_input ('input nilai SkinThickness')

Insulin = st.text_input ('input nilai insulin')

BMI	= st.text_input ('input nilai BMI')

DiabetesPedigreeFunction = st.text_input ('input nilai DiabetesPedigreeFunction')

Age = st.text_input ('input nilai Age')

diab_diagnosis = ''

if st.button('tes prediksi diabetes') :
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diab_prediction[0]==1):
        diab_diagnosis = 'pasien terkena diabetes'

    else :
        diab_diagnosis = 'pasien tidak terkena diabetes'

    st.success(diab_diagnosis)