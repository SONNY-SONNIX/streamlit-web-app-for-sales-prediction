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

# Load the trained decision tree model
# model = DecisionTreeRegressor()  # Replace with your trained model
decision_tree= DecisionTreeRegressor()
# Load the data used for prediction
#data = pd.read_csv('data')  # Replace with your data file or source
final_dataset = pd.read_csv('final_dataset.csv')

# Create the Streamlit web interface
st.title("Sales Prediction with Decision Tree")
st.write("Enter the input features and click 'Predict' to get the sales prediction.")

# Input form for user
input_form = st.form(key='sales_prediction_form')
#feature1 = input_form.number_input("Feature 1")
#feature2 = input_form.number_input("Feature 2")
BinaryEncoder = input_form.number_input["encoder_1"]
OrdinalEncoder= input_form.number_input["encoder_2"]
# Add more input features as necessary

predict_button = input_form.form_submit_button('Predict')

# Perform prediction when the 'Predict' button is clicked
if predict_button:
    # Prepare the input features as a DataFrame for prediction
    input_data = pd.DataFrame({
        'BinaryEncoder': [encoder_1],
        'OrdinalEncoder': [encoder_2]
        # Add more input features as necessary
    })
    
    # Make the sales prediction using the trained model
    prediction = decision_tree.predict(input_data)

    # Display the prediction result
    st.subheader("Sales Prediction")
    st.write("The predicted sales value is:", prediction)


