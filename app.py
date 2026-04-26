import streamlit as st
import pandas as pd
import joblib

# Load model + columns
model = joblib.load("model/house_price_model.pkl")
model_columns = joblib.load("model/model_columns.pkl")

st.title("🏠 House Price Prediction")

# Inputs
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sq ft)", 500, 5000, 1500)
garage_cars = st.number_input("Garage Capacity", 0, 5, 1)
total_bsmt = st.number_input("Basement Area", 0, 3000, 500)
year_built = st.number_input("Year Built", 1900, 2025, 2000)

if st.button("Predict"):
    input_dict = {
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt,
        "YearBuilt": year_built
    }

    input_df = pd.DataFrame([input_dict])

    # Convert + align with training data
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)

    st.success(f"Estimated Price: ${prediction[0]:,.2f}")