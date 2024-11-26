import os
import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

import subprocess
import sys
import streamlit as st



# Set page configuration
st.set_page_config(page_title="price prediction",
                   layout="wide",
                   page_icon="🚗")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

car_model = pickle.load(open(f'{working_dir}/car_price.sav', 'rb'))
gold_model = pickle.load(open(f'{working_dir}/gold_price.sav', 'rb'))
house_model = pickle.load(open(f'{working_dir}/house_price.sav', 'rb'))

# Sample data (replace with your actual dataset)
with st.sidebar:
    selected = option_menu('Price Prediction System',

                           ['Car Price Prediction',
                            'Gold Price Prediction',
                            'House Price Prediction'],
                           menu_icon='currency-exchange',
                           icons=['inboxes-fill', 'strava', 'houses'],
                           default_index=0)



if selected == 'Car Price Prediction':

    st.title('Car Price Predcition')

    car_name=st.text_input('car name')
    year=st.number_input("year", value=2000)
    Present_Price=st.number_input("present_price", value=0.0)
    Kms_Driven=st.number_input("Kms_Driven", value=1000)

    # Encoding the 'Fuel_Type' column
    fuel_type = st.selectbox('Choose Fuel Type:', ['Petrol', 'Diesel', 'CNG'])
    fuel_mapping = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
    fuel_type_encoded = fuel_mapping[fuel_type]

    # Encoding the 'Seller_Type' column
    seller_type = st.selectbox('Choose Seller Type:', ['Dealer', 'Individual'])
    seller_mapping = {'Dealer': 0, 'Individual': 1}
    seller_type_encoded = seller_mapping[seller_type]

    # Encoding the 'Transmission' column
    transmission = st.selectbox('Choose Transmission Type:', ['Manual', 'Automatic'])
    transmission_mapping = {'Manual': 0, 'Automatic': 1}
    transmission_encoded = transmission_mapping[transmission]

    owner=st.number_input("owner", value=0)


    if st.button('car price'):
        input_data = [year,Present_Price,Kms_Driven,fuel_type_encoded,seller_type_encoded,transmission_encoded,owner]

        input_data = [float(x) for x in input_data]

        car_pred =car_model.predict([input_data])
        #st.write(car_pred)

        st.success(car_pred)

if selected == 'Gold Price Prediction':
    st.title('Gold Price Prediction')
    spx=st.number_input("spx", value=1000.0)
    uso=st.number_input("uso", value=10.0)
    slv=st.number_input("slv", value=10.0)
    Eur=st.number_input("Eur/Usd", value=1.0)
    if st.button('Gold price'):
        input_data = [spx,uso,slv,Eur]

        input_data = [float(x) for x in input_data]

        gold_pred =gold_model.predict([input_data])
        #st.write(car_pred)

        st.success(gold_pred)

if selected == 'House Price Prediction':

    st.title('House Price Predcition')
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        crim=st.number_input("Crime_Rate", value=0.0)

    with col2:
        zn=st.number_input("Residential_Area", value=0.0)

    with col3:
        indus=st.number_input("Industry_Area", value=0.0)

    with col4:
        chas=st.number_input("Charles_River_Dummy", value=0.0)

    with col5:
        nox=st.number_input("Nitrogen_Oxide_Concentration", value=0.0)


    with col1:
        rm=st.number_input("Average_Rooms", value=0.0)

    with col2:
        age=st.number_input("Proportion_of_Owner_Occupied_Units", value=0.0)

    with col3:
        dis=st.number_input("Distance_to_Employment_Centers", value=0.0)

    with col4:
        rad=st.number_input("Accessibility_to_Radial_Highways", value=0.0)

    with col5:
        tax=st.number_input("Property_Tax_Rate", value=100.0)


    with col1:
        ptratio=st.number_input("Pupil_to_Teacher_Ratio", value=10.0)

    with col2:
        b=st.number_input("Proportion_of_Blacks_in_Area", value=100.0)

    with col3:
        lstat=st.number_input("Percentage_of_Lower_Socioeconomic_Status", value=0.0)
    
    
    
    if st.button('House price'):
        input_data = [crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]

        input_data = [float(x) for x in input_data]

        house_pred =house_model.predict([input_data])
        #st.write(car_pred)

        st.success(house_pred)
