# 🚗 Car Price Prediction using Multiple Linear Regression

This project predicts the price of a car using Multiple Linear Regression based on key engine and performance features.

It uses Scikit-Learn for model training and evaluation, along with data preprocessing and visualization.

---

## 📂 Project Structure

car_price
├── car_predict.py
├── CarPrice_Assignment.csv
├── Data Dictionary - carprices.xlsx
├── requirements.txt
└── README.md

---

##  Dataset

Dataset used:
CarPrice_Assignment.csv

The dataset contains multiple car attributes. For this project, only numerical performance-related features were used after dropping categorical columns.

### Features Used in Model:
- Engine Size
- Bore Ratio
- Stroke
- Compression Ratio
- Horsepower
- Peak RPM
- City MPG

Target Variable:
- Price

---

##  Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn

---

##  Machine Learning Model

Model Used:
Multiple Linear Regression

Steps performed:

1. Load dataset
2. Drop categorical features
3. Remove less relevant correlated features
4. Split dataset (60% train / 40% test)
5. Standardize features using StandardScaler
6. Train Linear Regression model
7. Evaluate using:
   - Mean Absolute Error (MAE)
   - Mean Squared Error (MSE)
   - R² Score
8. Predict custom user input

---

##  Model Evaluation Metrics

The script prints:

- Mean Absolute Error
- Mean Squared Error
- R² Score

These help evaluate how well the model fits unseen data.

---

##  How to Run

###  Install dependencies

```bash
pip install -r requirements.txt
```
### Run the script
```
python car_predict.py
```

### Enter car details when prompted
## 📌 Notes

- Scaling is applied before training.
- The scaler is fit only on training data.
- The same scaler is used to transform user input.
- Random state is fixed (42) for reproducibility.

---

## 📊 Evaluation Metrics

| Metric | Meaning |
|--------|---------|
| MAE | Average absolute error |
| MSE | Average squared error |
| R² | Model accuracy score |

---

## 🧪 Possible Improvements

- Save trained model using `joblib`
- Add visualization of regression results
- Deploy as Flask API
- Use cross-validation
- Add polynomial regression comparison

---

## 👨‍💻 Author

Parth Petkar

---

## 📜 License

This project is open-source and free to use.

