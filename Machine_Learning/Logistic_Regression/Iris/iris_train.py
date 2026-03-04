#----------------------------------Flower Classification Using Logistic Regression-----------------------------------------------

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load Dataset
iris=load_iris()

# Separate the Features and Labels
X=iris.data
y=iris.target

# Store Features and Class Names
feature_names=iris.feature_names
target_names=iris.target_names

# Load as Pandas DataFrame
df=pd.DataFrame(X,columns=feature_names)
df['species']=y

# Map Numerics with Specific Species
df['species']=df['species'].map({
    0: "setosa",
    1: "versicolor",
    2: "virginica"
})

# Explanatory Data Analysis
print(df.head())
print(df.describe())
print(df["species"].value_counts())

# Visualize the Features
sns.pairplot(df, hue="species")
plt.show()

# Extract Features and Labels
X = df.drop("species", axis=1)
y = df["species"]

# Create a Train and Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the Logistic Regression Model
LR=linear_model.LogisticRegression(max_iter=200)

# Train the Model
LR.fit(X_train,y_train)

# Predict Test Data
y_pred=LR.predict(X_test)

# Model Evaluation
# Accuracy Score
print("Accuracy: ", accuracy_score(y_test, y_pred))

# Confusion Matrix 
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=target_names, yticklabels=target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Save the Model
joblib.dump(LR,"iris_train.pkl")
print("Model Saved!")