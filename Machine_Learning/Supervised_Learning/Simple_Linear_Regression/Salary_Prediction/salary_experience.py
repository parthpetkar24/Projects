import pandas as pd                                                             # Data Handling Library
import numpy as np                                                              # Numerical Computing
import matplotlib.pyplot as plt                                                 # Visualization
from sklearn import linear_model                                                # Machine Learning Library
from sklearn.model_selection import train_test_split                            # Split data into training and testing set
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score     # Measuring the correctness of model
import os                                                                       # For file path

# Function that Predicts Salary based on Experience
def salarypredict(user_exp,show_graph,show_metrice):

    # File Path Handling
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(BASE_DIR,"salary_experience.csv")

    # Loading the Dataset
    data=pd.read_csv(file_path)
    # print(data)

    #Visualizing the existing dataset
    if show_graph=="y":
        plt.scatter(data.YearsExperience,data.Salary,color='red')
        plt.xlabel('YearsExperience')
        plt.ylabel('Salary')
        plt.show()

    # Extracting Features and Labels from the dataset and converting them to array as ML Model work on Array and Matrices
    x_experience=data.YearsExperience.to_numpy()
    y_salary=data.Salary.to_numpy()

    # Creating a Train and Test Split of Data for 20% data for testing and 80% for training
    x_train,x_test,y_train,y_test=train_test_split(x_experience,y_salary,test_size=0.2,random_state=24)

    # Creating A Linear Regression Model 
    regressor=linear_model.LinearRegression()

    # ML model expects 2D Matrix so we reshape the training model
    # ML uses Ordinary Least Square to find the intercept and slope
    regressor.fit(x_train.reshape(-1,1),y_train)

    # Slope and Intercept
    slope=regressor.coef_[0]
    intercept=regressor.intercept_

    # Visualizing Regression Graph
    if show_graph=="y":
        plt.scatter(x_train,y_train,color='red')
        x_line = np.sort(x_train)
        plt.plot(x_line,(slope*x_line)+intercept,'-g')
        plt.xlabel("Experience")
        plt.ylabel("Salary")
        plt.show()

    # Predict data on test data
    y_pred=regressor.predict(x_test.reshape(-1,1))
    if show_metrice=="y":
        print(f"Slope: {slope}")
        print(f"Intercept: {intercept}")
        print(f"Mean Absolute Error: {mean_absolute_error(y_test,y_pred)}")
        print(f"Mean Squared Error: {mean_squared_error(y_test,y_pred)}")
        print(f"R2 Score: {r2_score(y_test,y_pred)}")

    # Predict on User Data
    salary_prediction=regressor.predict([[user_exp]])[0]
    return salary_prediction

# Main Block
if __name__=="__main__":
    user_exp=float(input("Enter User Experience: "))                            # Input User Experience
    see_graph=input("See Graphs? (y/n): ").lower()                              # Does User want to see graphs?
    see_metrice=input("See Metrices? (y/n): ").lower()                          # Does User want to see metrices?
    print(f"Salary Expected= {salarypredict(user_exp,see_graph,see_metrice)}")  # Function call and display prediction