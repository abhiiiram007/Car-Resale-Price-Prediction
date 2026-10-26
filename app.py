import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------------
# Page config
# ---------------------------------------------------------
st.set_page_config(page_title="Car Resale Price Predictor", page_icon="🚗", layout="centered")

st.title("🚗 Car Resale Price Predictor")
st.write("Enter your car's details below to get an estimated resale price.")

# ---------------------------------------------------------
# Load model + scaler
# ---------------------------------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("car_resale_price_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

try:
    model, scaler = load_artifacts()
except FileNotFoundError:
    st.error(
        "Model files not found. Place 'car_resale_price_model.pkl' "
        "and 'scaler.pkl' in the same folder as this app."
    )
    st.stop()

# ---------------------------------------------------------
# User Inputs
# ---------------------------------------------------------
st.subheader("Car Details")

col1, col2 = st.columns(2)

with col1:
    engine_capacity = st.number_input(
        "Engine Capacity (cc)", min_value=600, max_value=6000, value=1200, step=50
    )
    kms_driven = st.number_input(
        "Kilometers Driven", min_value=0, max_value=500000, value=30000, step=1000
    )
    car_age = st.number_input(
        "Car Age (years)", min_value=0, max_value=30, value=3, step=1
    )

with col2:
    fuel_type = st.selectbox(
        "Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
    )
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

st.divider()


DEFAULT_SEATS = 5
DEFAULT_MILEAGE = 18.0  

with st.expander("Advanced (optional)"):
    seats = st.number_input("Seats", min_value=2, max_value=10, value=DEFAULT_SEATS, step=1)
    mileage = st.number_input(
        "Mileage (kmpl)", min_value=5.0, max_value=40.0, value=DEFAULT_MILEAGE, step=0.5
    )

# ---------------------------------------------------------
# Predict
# ---------------------------------------------------------
if st.button("🔮 Predict Resale Price", use_container_width=True):

    input_dict = {
        "engine_capacity": [engine_capacity],
        "kms_driven": [kms_driven],
        "seats": [seats],
        "mileage": [mileage],
        "car_age": [car_age],
        "transmission_type_Automatic": [1 if transmission == "Automatic" else 0],
        "transmission_type_Manual": [1 if transmission == "Manual" else 0],
        "fuel_type_CNG": [1 if fuel_type == "CNG" else 0],
        "fuel_type_Diesel": [1 if fuel_type == "Diesel" else 0],
        "fuel_type_Electric": [1 if fuel_type == "Electric" else 0],
        "fuel_type_LPG": [1 if fuel_type == "LPG" else 0],
        "fuel_type_Petrol": [1 if fuel_type == "Petrol" else 0],
    }

    sample = pd.DataFrame(input_dict)

    # IMPORTANT: column order must match training-time column order exactly
    expected_cols = [
        "engine_capacity", "kms_driven", "seats", "mileage", "car_age",
        "transmission_type_Automatic", "transmission_type_Manual",
        "fuel_type_CNG", "fuel_type_Diesel", "fuel_type_Electric",
        "fuel_type_LPG", "fuel_type_Petrol",
    ]
    sample = sample[expected_cols]

    sample_scaled = scaler.transform(sample)
    prediction = model.predict(sample_scaled)[0]  # model was trained on price/100000 (Lakhs)

    st.success(f"### Estimated Resale Price: ₹{prediction:,.2f} Lakhs")
    st.caption(f"(That's approximately ₹{prediction * 100000:,.0f})")
