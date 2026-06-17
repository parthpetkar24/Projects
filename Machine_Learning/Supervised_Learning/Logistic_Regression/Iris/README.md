# 🌸 Iris Flower Classification

A machine learning project that classifies iris flowers into three species — **Setosa**, **Versicolor**, and **Virginica** — using Logistic Regression.

---

## 📁 Project Structure

```
Iris/
├── iris_train.py       # Train the model and save it to disk
├── iris_predict.py     # Load the model and predict via CLI input
├── iris_train.pkl      # Saved trained model (generated after training)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

Run the training script to perform EDA, train the Logistic Regression model, evaluate it, and save the model file:

```bash
python iris_train.py
```

This will:
- Display a pairplot of the iris features
- Print accuracy score and a confusion matrix heatmap
- Save the trained model as `iris_train.pkl`

### 3. Make Predictions

Run the prediction script and enter flower measurements when prompted:

```bash
python iris_predict.py
```

**Example input:**
```
Enter flower measurements
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
Predicted species: setosa
```

---

## 📊 Dataset

The project uses the built-in [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) from `sklearn.datasets`, which contains **150 samples** across 3 species with 4 features each:

| Feature | Description |
|---|---|
| Sepal Length (cm) | Length of the sepal |
| Sepal Width (cm) | Width of the sepal |
| Petal Length (cm) | Length of the petal |
| Petal Width (cm) | Width of the petal |

---

## 📦 Requirements

See `requirements.txt` for all dependencies.
