from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib
import pandas as pd

from data_preprocessing import load_data, preprocess_data

# Load + preprocess
df = load_data("data/data.csv")  # correct file
X, y = preprocess_data(df)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

importances = pd.Series(model.feature_importances_, index=X.columns)
print(importances.sort_values(ascending=False).head(10))

# Evaluate
pred = model.predict(X_test)
print("R2:", r2_score(y_test, pred))

# Save model + columns
joblib.dump(model, "model/house_price_model.pkl")
joblib.dump(X.columns.tolist(), "model/model_columns.pkl")