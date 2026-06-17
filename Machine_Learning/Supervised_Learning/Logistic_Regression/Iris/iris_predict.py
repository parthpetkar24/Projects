#--------------------------------------------CLI Execution of Iris Model---------------------------------------------------------
# Import Libraries
import joblib
import pandas as pd

# Load Trained Model
predict_model=joblib.load("iris_train.pkl")

# Define Species
species = ["setosa", "versicolor", "virginica"]

#Take User Input
print("Enter flower measurements")
sl = float(input("Sepal Length: "))
sw = float(input("Sepal Width: "))
pl = float(input("Petal Length: "))
pw = float(input("Petal Width: "))

# Make Predictions
sample = pd.DataFrame(
    [[sl, sw, pl, pw]],
    columns=[
        'sepal length (cm)',
        'sepal width (cm)',
        'petal length (cm)',
        'petal width (cm)'
    ]
)

prediction = predict_model.predict(sample)

print("Predicted species:", prediction[0])