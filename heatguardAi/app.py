import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# Load trained model
model = joblib.load("heatguardAi/model.pkl")

# Page configuration
st.set_page_config(
    page_title="HeatGuard AI",
    page_icon="🔥",
    layout="wide"
)

# Title
st.title("🔥 HeatGuard AI")
st.subheader("Urban Heat Risk Prediction System")

# Sidebar Inputs
st.sidebar.header("🌦️ Weather Parameters")

temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=20,
    max_value=50,
    value=30
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=20,
    max_value=100,
    value=60
)

windspeed = st.sidebar.slider(
    "Wind Speed (km/h)",
    min_value=1,
    max_value=20,
    value=10
)

# Display Current Values
st.write("## Current Values")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperature", f"{temperature}°C")

with col2:
    st.metric("💧 Humidity", f"{humidity}%")

with col3:
    st.metric("💨 Wind Speed", f"{windspeed} km/h")

# Prediction Button
if st.button("🚀 Predict Heat Risk"):

    try:
        # Predict
        prediction = model.predict(
            [[temperature, humidity, windspeed]]
        )[0]

        st.write("## Prediction Result")

        # If model returns numbers
        if prediction == 2:
            st.error("🔴 HIGH HEAT RISK")

        elif prediction == 1:
            st.warning("🟡 MEDIUM HEAT RISK")

        elif prediction == 0:
            st.success("🟢 LOW HEAT RISK")

        # If model returns text labels
        elif str(prediction).lower() == "high":
            st.error("🔴 HIGH HEAT RISK")

        elif str(prediction).lower() == "medium":
            st.warning("🟡 MEDIUM HEAT RISK")

        else:
            st.success("🟢 LOW HEAT RISK")

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# Footer
st.markdown("---")
st.caption("HeatGuard AI | Urban Heat Risk Prediction System")
