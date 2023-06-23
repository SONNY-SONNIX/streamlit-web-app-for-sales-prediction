## Packages imported
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import streamlit as st 
from PIL import Image
import pickle 
import datetime
import os


# Utils 

# Setup & config


# App 

# Load the trained decision tree model from the pickle file
model_path = 'decision_tree_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit app layout
st.title('Sales Prediction')
st.write('Enter a date to predict sales:')
date = st.date_input('Date')

# Predict sales when the predict button is clicked
if st.button('Predict'):
    # Perform any necessary preprocessing on the date input, e.g., feature engineering
    
    # Make the prediction using the trained model
    prediction = model.predict([date])  # Replace [date] with the preprocessed input
    
    # Display the predicted sales
    st.write(f'Predicted sales for {date}: {prediction}')



