import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("heat_data.csv")

X = data[["Temperature","Humidity","WindSpeed"]]
y = data["HeatRisk"]

model = RandomForestClassifier(
n_estimators=200,
random_state=42
)

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully")
import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("🔥 HeatGuard AI")

temperature = st.slider("Temperature", 20, 50, 30)
humidity = st.slider("Humidity", 20, 100, 60)
windspeed = st.slider("Wind Speed", 1, 20, 10)

if st.button("Predict Heat Risk"):

```
prediction = model.predict(
    [[temperature, humidity, windspeed]]
)[0]

st.write("Prediction:", prediction)
```
