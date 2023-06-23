## Packages imported
import streamlit as st 
import pandas as pd
#from sklearn.tree import DecisionTreeRegressor
import numpy as np
from PIL import Image
import pickle 
import datetime
import os
from sklearn.tree import DecisionTreeRegressor



# Utils 

# Setup & config


# App 
# Set page title and layout 
st.set_page_config(page_title="Favorita Stores Sales Prediction App",layout="centered")

#Image loader 
st.image("screenshots\hour_glass_2.jpg")

data_dt = {"model":decision_tree,"encoder_1":BinaryEncoder,"encoder_2":OrdinalEncoder}
# Load the trained decision tree model from the pickle file
#model_path = 'saved.pkl'
model_path = "src\saved.pkl"
def load_model():
    if os.path.exists("model_path"):
        #File exists perform operations on it 
        with open(model_path, 'rb') as file:
    #model = pickle.load(file)
        data_dt = pickle.load(file)
        return data_dt    
    else:
    # File does not exist, handle the scenario
        print("The 'saved' file does not exist.")        

# Streamlit app layout
st.title('Favorita Stores Sales Prediction App')
st.write('Enter a date to predict sales:')
date = st.date_input('Date')

# Predict sales when the predict button is clicked
if st.button('Predict'):
    # Perform any necessary preprocessing on the date input, e.g., feature engineering
    decision_tree = data_dt["model"]
    BinaryEncoder = data_dt["encoder_1"]
    OrdinalEncoder = data_dt["encoder_2"]

    # Make the prediction using the trained model
    #prediction = model.predict([date])  # Replace [date] with the preprocessed input
    prediction = data_dt.predict([decision_tree])

    # Display the predicted sales
    #st.write(f'Predicted sales for {date}: {prediction}')

