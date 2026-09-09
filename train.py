import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def train_and_save_model():
    print("--- Training Height Prediction Model ---")

    # 1. Dataset Initialization
    data = {
        'Weight_kg': [50, 60, 65, 70, 75, 80, 85, 90, 95, 100],
        'Height_cm': [155, 162, 165, 170, 174, 178, 181, 185, 188, 192]
    }
    df = pd.DataFrame(data)

    X = df[['Weight_kg']]
    y = df['Height_cm']

    # 2. Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Model Training
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 4. Model Evaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Learned Slope (w): {model.coef_[0]:.2f}")
    print(f"Learned Intercept (b): {model.intercept_:.2f}")
    print(f"Mean Absolute Error (MAE): {mae:.2f} cm")
    print(f"R² Score: {r2:.4f}\n")

    # 5. Save Model Artifact
    model_path = "model.joblib"
    joblib.dump(model, model_path)
    print(f"✅ Model successfully saved to '{model_path}'!")

if __name__ == "__main__":
    train_and_save_model()