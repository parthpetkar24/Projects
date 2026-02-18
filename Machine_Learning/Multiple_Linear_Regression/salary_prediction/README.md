# 💼 Salary Predictor Using Multiple Linear Regression

A machine learning project that predicts employee salaries based on experience metrics using Multiple Linear Regression.

---

## 📌 Overview

This project builds a salary prediction model trained on professional experience data. It uses **Multiple Linear Regression** to learn the relationship between an employee's experience profile and their expected salary.

---

## 📂 Dataset

The dataset is sourced from GitHub and contains the following features:

| Feature | Description |
|---|---|
| `Total Experience` | Total years of professional experience |
| `Team Lead Experience` | Years spent in a team lead role |
| `Project Manager Experience` | Years spent in a project manager role |
| `Certifications` | Number of certifications held *(dropped — weak correlation)* |
| `Salary` | Target variable — employee salary |

---

## 🔧 Tech Stack

- **Python 3**
- **pandas** — data loading and manipulation
- **NumPy** — numerical operations
- **matplotlib** — data visualization
- **scikit-learn** — preprocessing, model training, and evaluation

---

## 🚀 How It Works

1. **Load Data** — reads the CSV dataset directly from a GitHub URL
2. **Exploratory Analysis** — computes a Pearson correlation matrix to assess feature relevance
3. **Feature Selection** — drops `Certifications` due to weak correlation with salary
4. **Visualization** — generates a scatter matrix (pairwise plots) across all features
5. **Train/Test Split** — splits data 60/40 for training and testing
6. **Preprocessing** — applies `StandardScaler` to normalize feature values
7. **Model Training** — fits a `LinearRegression` model on scaled training data
8. **Regression Plots** — visualizes each feature's linear relationship with salary
9. **Evaluation** — reports MAE, MSE, and R² score on the test set

---

## 📊 Model Evaluation Metrics

| Metric | Description |
|---|---|
| **MAE** | Mean Absolute Error — average prediction error in salary units |
| **MSE** | Mean Squared Error — penalizes larger errors more heavily |
| **R² Score** | Proportion of variance in salary explained by the model |

---

## ▶️ Usage

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd salary-predictor
```

**2. Install dependencies**
```bash
pip install pandas numpy matplotlib scikit-learn
```

**3. Run the script**
```bash
python salary_predictor.py
```

---

## 📁 Project Structure

```
salary-predictor/
│
├── salary_predictor.py   # Main script
└── README.md             # Project documentation
```

---

This project is open source and available for educational purposes.