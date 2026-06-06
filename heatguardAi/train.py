import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("heat_data.csv")

X = data[["Temperature","Humidity","WindSpeed"]]
y = data["HeatRisk"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X,y)

joblib.dump(model,"model.pkl")

print("🔥 HeatGuard AI Model Trained Successfully")