import pandas as pd

import streamlit as st

import pickle as pkl

import warnings

warnings.filterwarnings('ignore')

model = pkl.load(open('Linearmodel.pkl','rb'))

st.header('House Price Prediction')

Area = st.slider('Select Area in Sqft',800,7000)

No_Bedrooms = st.slider('Select No of Bedrooms',1,5)

Age_House = st.slider('Select How Many Years House Old',1,25)

if st.button('Predict'):
    
    data = [[Area,No_Bedrooms,Age_House]]
    prediction = model.predict(data)
    
    st.markdown(f"<h1 style='text-align : center;'>Predicting Price is : {prediction[0]:.2f}</h1>",unsafe_allow_html=True)