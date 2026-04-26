import joblib
import pandas as pd

from data_preprocessing import preprocess_data

# Load model
model = joblib.load("model/house_price_model.pkl")

def predict(input_df):
    X, _ = preprocess_data(input_df)
    return model.predict(X)