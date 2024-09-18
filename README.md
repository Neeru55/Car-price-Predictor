# Car Price Predictor

This project aims to predict the selling price of cars using machine learning models. It includes a Jupyter notebook for data preprocessing, model training, and evaluation, and a Streamlit application for real-time predictions.

## Project Structure

- **`car price prediction.ipynb`**: A Jupyter notebook that performs data cleaning, feature engineering, model training, and evaluation. It processes the dataset, trains various regression models, and evaluates their performance. The best-performing model is saved for use in the Streamlit app.
- **`app.py`**: A Streamlit application script that uses the trained model to make predictions based on user input through an interactive web interface.

## Prerequisites

Before running the Jupyter notebook or the Streamlit app, ensure you have the following Python packages installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `streamlit`
- `pickle`

Install the required packages using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
 ```
##Setup and Usage
Jupyter Notebook (car price prediction.ipynb)
#Download the Dataset:

Ensure that you have the dataset file named Car details v3.csv placed in a directory named DATASET.
#Run the Notebook:

Open the car price prediction.ipynb notebook in Jupyter.
Execute all cells to perform the following tasks:
Load and clean the dataset.
Perform feature engineering and encode categorical variables.
Train multiple machine learning models (Linear Regression, Decision Tree, Random Forest).
Evaluate models and save the best model (RandomForestRegressor) as model.pkl.
#Save the Model:

The notebook saves the trained Random Forest model as model.pkl in the working directory.
##Streamlit Application (app.py)
#Prepare the Model and Dataset:

Ensure model.pkl (saved from the Jupyter notebook) and Car details v3.csv (dataset file) are in the same directory as app.py.
#Run the Streamlit App:

Open a terminal or command prompt.

Navigate to the directory containing app.py.

Run the Streamlit app using the following command:

```bash
streamlit run app.py
 ```
#Interact with the App:

Use the Streamlit sidebar to provide details about the car.
Adjust the sliders and dropdown menus for the car’s features.
Click the "Predict" button to get an estimated price for the car.
The predicted price will be displayed at the bottom of the page.
Use the Streamlit sidebar to provide details about the car.
Adjust the sliders and dropdown menus for the car’s features.
Click the "Predict" button to get an estimated price for the car.
The predicted price will be displayed at the bottom of the page.
##Data Description
The dataset Car details v3.csv contains the following features:

name: Car brand and model.
year: Manufacturing year of the car.
km_driven: Number of kilometers driven.
fuel: Fuel type (e.g., Diesel, Petrol).
seller_type: Type of seller (e.g., Individual, Dealer).
transmission: Transmission type (e.g., Manual, Automatic).
owner: Number of previous owners.
mileage: Mileage in km/l.
engine: Engine capacity in cc.
max_power: Maximum power in bhp.
seats: Number of seats.
selling_price: Price of the car (target variable).
##Model
The best-performing model, RandomForestRegressor, is used for predicting car prices based on the input features. The model was trained and evaluated in the Jupyter notebook and saved as model.pkl for use in the Streamlit app.
use this to run app.py 
streamlit run app.py
