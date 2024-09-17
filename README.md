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

