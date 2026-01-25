# Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
import os

# Function to predict the score for hours
def score_predict(user_hours,show_plots,show_metrices):

    # Checks for the dataset file
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(BASE_DIR,"rounded_hours_student_scores.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError("Dataset file not found")
    
    # Load data from csv file using pandas
    data=pd.read_csv(file_path)
    # print(data)

    # If User wants visualize the pre-existing data
    if show_plots=='y':
        plt.scatter(data.Hours,data.Scores,color='red')
        plt.xlabel('Hours')
        plt.ylabel('Scores')
        plt.show()

    # Extract the features and labels from dataset, store as numpy array
    x_hours=data.Hours.to_numpy()
    y_scores=data.Scores.to_numpy()

    # Create train and test datasets
    x_train,x_test,y_train,y_test=train_test_split(x_hours,y_scores,test_size=0.2,random_state=24)

    # Linear Regression Model and a model object named 'regressor'
    regressor=linear_model.LinearRegression()

    # sklearn expects a 2D array as input with (n_observation, n_features), so reshape x_train as 2D
    regressor.fit(x_train.reshape(-1,1),y_train)

    # Store the coeeficient and intercept
    slope=regressor.coef_[0]
    intercept=regressor.intercept_

    # If User wants visualize the Model Output
    if show_plots=='y':
        plt.scatter(x_train,y_train,color='red')
        x_line = np.sort(x_train)
        plt.plot(x_line,(slope*x_line)+intercept,'-g')
        plt.xlabel("Hours")
        plt.ylabel("Scores")
        plt.show()

    # Make Predictions using predict function
    y_pred=regressor.predict(x_test.reshape(-1,1))

    # If User wants show the Model Evaluation
    if show_metrices=='y':
        print(f"Slope/Coeffiecient= {slope}")
        print(f"Intercept= {intercept}")
        print(f"Mean Absolute Error: {mean_absolute_error(y_test,y_pred)}")
        print(f"Mean squared Error: {mean_squared_error(y_test,y_pred)}")
        print(f"R2 Score: {r2_score(y_test,y_pred)}")

    # Predict the score for User Input
    predict_score=regressor.predict([[user_hours]])[0]
    return predict_score

if __name__ == "__main__"  :
    # Take User Hours as input
    user_hours=float(input("Enter Number of Hours Studied: "))

    # Check if User wants to visualize the graph or review evaluation or both
    see_plot = input("See Graphs? (y/n): ").lower() 
    see_metrices = input("See Metrics? (y/n): ").lower()

    # Display the prediction
    print(f"Score Prediction: {score_predict(user_hours,see_plot,see_metrices)}")

