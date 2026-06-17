# 🏠 House Price Prediction using Multiple Linear Regression

This project predicts house prices based on:

- Area (square feet)
- Number of Bedrooms
- Age of the House

The model uses **Multiple Linear Regression** with feature scaling.

---

## 📂 Project Structure

```
house_price
├── homeprices.py
├── homeprices.csv
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset (`homeprices.csv`) must contain the following columns:

- `area`
- `bedrooms`
- `age`
- `price`

Missing values in the `bedrooms` column are handled using the median.

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib

---

## 🧠 Machine Learning Workflow

1. Load dataset
2. Handle missing values (median imputation)
3. Select features (area, bedrooms, age)
4. Train-test split (60% training, 40% testing)
5. Apply feature scaling using `StandardScaler`
6. Train `LinearRegression` model
7. Evaluate using:
   - MAE (Mean Absolute Error)
   - MSE (Mean Squared Error)
   - R² Score
8. Predict new house price based on user input

---

## 📈 Model Used

Multiple Linear Regression:

Price = b0 + b1(area) + b2(bedrooms) + b3(age)

Where:
- b0 = intercept
- b1, b2, b3 = coefficients

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd <repo-folder>
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the program

```
python homeprices.py
```

---

## 🖥 Example Input

```
Enter Area in sq. ft. : 3000
Enter Number of Bedrooms: 3
Enter Age of House: 15
```

Output:

```
MAE: ...
MSE: ...
R2 Score: ...
Predicted House Price = ...
```

---

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
