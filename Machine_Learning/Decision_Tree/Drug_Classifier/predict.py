import joblib
import pandas as pd

# Load model
model = joblib.load("drug_model.pkl")

# Load encoders
sex_encoder = joblib.load("sex_encoder_model.pkl")
bp_encoder = joblib.load("bp_encoder_model.pkl")
chol_encoder = joblib.load("cnhol_encoder_model.pkl")

# User Input
age = int(input("Enter Age: "))
sex = input("Enter Sex (F/M): ")
bp = input("Enter BP (HIGH/LOW/NORMAL): ")
chol = input("Enter Cholesterol (HIGH/NORMAL): ")
na_to_k = float(input("Enter Sodium to Potassium Ratio: "))

# Encode categorical values
sex_encoded = sex_encoder.transform([sex])[0]
bp_encoded = bp_encoder.transform([bp])[0]
chol_encoded = chol_encoder.transform([chol])[0]

# Create dataframe
input_data = pd.DataFrame([[
    age,
    sex_encoded,
    bp_encoded,
    chol_encoded,
    na_to_k
]], columns=[
    'Age',
    'Sex',
    'BP',
    'Cholesterol',
    'Na_to_K'
])

# Prediction
prediction = model.predict(input_data)

print("\nPredicted Drug:", prediction[0])