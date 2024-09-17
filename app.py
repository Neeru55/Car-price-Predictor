import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

# Load the pre-trained model with error handling
try:
    model = pk.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please check the file path.")
    st.stop()

# Set up the Streamlit header
st.markdown("<h1 style='text-align: center; color: white;'>Car Price Prediction ML Model</h1>", unsafe_allow_html=True)

# Load the dataset with error handling
try:
    cars_data = pd.read_csv('Car details v3.csv')
except FileNotFoundError:
    st.error("Dataset not found. Please check the file path.")
    st.stop()

# Sidebar for additional information
st.sidebar.title("About the App")
st.sidebar.info("""
This app predicts the price of a car based on various input features like brand, year, kilometers driven, and more.
It utilizes a pre-trained machine learning model to provide accurate predictions.
""")
st.sidebar.markdown("<h3 style='color: white;'>Instructions</h3>", unsafe_allow_html=True)
st.sidebar.write("""
1. Fill in the details of the car on the left.
2. Press the "Predict" button to get the estimated price.
3. The predicted price will appear at the bottom of the page.
""")

# Custom CSS for dark theme
st.markdown(
    """
    <style>
    body {
        background-color: #2B2B2B;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
    }
    .stButton>button {
        background-color: #00b4d8;
        color: white;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #0077b6;
    }
    </style>
    """, unsafe_allow_html=True
)

# Function to extract the brand name from the car name
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()

# Apply the function to extract brand names
cars_data['name'] = cars_data['name'].apply(get_brand_name)

# UI Components for the app
name = st.selectbox('Select Car Brand', cars_data['name'].unique())
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('Number of Kilometers Driven', 11, 200000)
fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller Type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
owner = st.selectbox('Ownership Type', cars_data['owner'].unique())
mileage = st.slider('Car Mileage (kmpl)', 10.0, 40.0)
engine = st.slider('Engine Capacity (cc)', 700, 5000)
max_power = st.slider('Max Power (bhp)', 0, 200)
seats = st.slider('Number of Seats', 4, 10)

# Prediction button
if st.button("Predict"):
    # Preparing input data for the model
    input_data_model = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
    )

    # Converting categorical data into numerical values for the model
    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'],
                                      [1, 2, 3, 4, 5], inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata',
                                      'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen',
                                      'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat',
                                      'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                      24, 25, 26, 27, 28, 29, 30, 31], inplace=True)

    # Predict the car price
    try:
        car_price = model.predict(input_data_model)
        # Display the predicted price
        st.success(f'The predicted price of the car is ₹ {round(car_price[0], 2):,.2f}')
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")
