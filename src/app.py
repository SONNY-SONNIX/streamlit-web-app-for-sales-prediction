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
#Image loader 
st.image("Z:\GitHub Space\streamlit-web-app-for-sales-prediction\screenshots\hour_glass.jpg")

st.set_page_config(page_title="Favorita Stores Sales Prediction App",layout="wide")

# Load the trained decision tree model from the pickle file

model_path = 'saved.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)


# Streamlit app layout
st.title('Favorita Stores Sales Prediction App')
st.write('Enter a date to predict sales:')
date = st.date_input('Date')


         

# Predict sales when the predict button is clicked
if st.button('Predict'):
    # Perform any necessary preprocessing on the date input, e.g., feature engineering
    
    # Make the prediction using the trained model
    prediction = model.predict([date])  # Replace [date] with the preprocessed input
    
    # Display the predicted sales
    st.write(f'Predicted sales for {date}: {prediction}')



