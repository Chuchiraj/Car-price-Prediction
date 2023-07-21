import pandas as pd
import numpy as np
import datetime as dt
import sklearn
import streamlit as st
from PIL import Image
import pickle
from sklearn.ensemble import RandomForestRegressor

model = pickle.load(open('model.sav','rb'))

st.title('Used Car Selling Price Prediction')
st.header('Enter the Car details')
#image = Image.open('background_Image.jpg')
#st.image(image,'')
#https://unsplash.com/photos/8e2gal_GIE8


def predict(Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner,car_age ):
    if Fuel_Type == 'CNG':
        Fuel_Type = 0
    elif Fuel_Type == 'Diesel':
        Fuel_Type = 1
    elif Fuel_Type == 'Petrol':
        Fuel_Type = 2
    if Seller_Type == 'Dealer':
        Seller_Type = 0
    elif Seller_Type == 'Individual':
        Seller_Type = 1
    if Transmission == 'Automatic':
        Transmission = 0
    elif Transmission == 'Manual':
        Transmission = 1
    if Owner == '1st Owner':
        Owner = 0
    elif Owner == '2nd Owner':
        Owner = 1
    elif Owner == '3rd Owner':
        Owner = 2
    elif Owner == '4th Owner':
        Owner = 3
    
    prediction = model.predict(pd.DataFrame( [[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, car_age]],
                                            columns=['Present_Price','Kms_Driven',
                                                      'Fuel_Type', 'Seller_Type', 'Transmission', 
                                                      'Owner', 'car_age' ] ))
    return prediction
    


Present_Price = st.number_input('Enter ex-showroom price in Lakh',min_value=0.00, step=0.01)
Kms_Driven = st.number_input('Enter current km reading',min_value=0, step=1)
Fuel_Type = st.selectbox('Enter Fuel Type',('Petrol' ,'Diesel' ,'CNG'))
Seller_Type = st.selectbox('Select the type you belong',('Individual' ,'Dealer'))
Transmission = st.selectbox('Enter Transmission Detail',('Manual' ,'Automatic'))
Owner = st.selectbox('Enter Owner Detail',('1st Owner' ,'2nd Owner','3rd Owner','4th Owner'))
car_year = st.number_input('Enter Mfg year',min_value=2000, max_value=2023, step=1)
car_age = dt.datetime.now().year - car_year

if st.button('Predict Car Price'):
    price = predict(Present_Price,  Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, car_age)
    st.success(f'The predicted price of your car is {price[0]:.2f} Lakh')
    #st.success(price[0])