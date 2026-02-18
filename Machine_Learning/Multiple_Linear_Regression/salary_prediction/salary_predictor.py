# ---------------------------------------- Salary Predictor Using Machine Learning----------------------------------------------

# Import Libraries 
import pandas as pd                                                         # Data Handling 
import numpy as np                                                          # Numerical Calculations and Array Handling
import matplotlib.pyplot as plt                                             # Visualization
from sklearn import linear_model                                            # Linear Model from sci-kit learn
from sklearn import preprocessing                                           # Data Preprocessing
from sklearn.model_selection import train_test_split                        # Creating Train and Test split for Model
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score # Model Evaluation 

# Load Data
# The dataset is uploaded on Github and the link is being used
data_path="https://raw.githubusercontent.com/parthpetkar24/Projects/refs/heads/main/Machine_Learning/Multiple_Linear_Regression/salary_prediction/data/SalaryMulti.csv"
data=pd.read_csv(data_path)

# Check if data is loaded
print(data.head(5))

# No categorical value present

# Check Correlated Matrix using Pearson correlation coefficient
print(data.corr())

# Since Certifications feature is weakly correlated to the target variable, removing it is best option
data=data.drop(['Certifications'],axis=1)

# Visualisation Scatter Matrix ,i.e., Pairwise Plots between features and target
axes=pd.plotting.scatter_matrix(data,alpha=0.2)
for ax in axes.flatten():
    ax.xaxis.label.set_rotation(90)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')
plt.tight_layout()
plt.gcf().subplots_adjust(wspace=0,hspace=0)
plt.show()

# Extract Features and Target
X=data[['Total Experience','Team Lead Experience','Project Manager Experience']].to_numpy()
Y=data['Salary'].to_numpy()

# Create Train and Test split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=42)

# Preprocess the data
# Standard Scaler to convert data in manageable range
std_scaler=preprocessing.StandardScaler()
x_train_scaled=std_scaler.fit_transform(x_train)
x_test_scaled=std_scaler.transform(x_test)

# Build Model
regressor=linear_model.LinearRegression()
regressor.fit(x_train_scaled,y_train)

# Coefficients extraction
b0=regressor.intercept_
b1,b2,b3=regressor.coef_

# Visualize the linear regression line of target with each feature
plt.scatter(x_train_scaled[:, 0],y_train)
plt.plot(x_train_scaled[:, 0],b0+(b1*x_train_scaled[:, 0]),'-g')
plt.xlabel("Total Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(x_train_scaled[:, 1],y_train)
plt.plot(x_train_scaled[:, 1],b0+(b2*x_train_scaled[:, 1]),'-g')
plt.xlabel("Team Lead Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(x_train_scaled[:, 2],y_train)
plt.plot(x_train_scaled[:, 2],b0+(b3*x_train_scaled[:, 2]),'-g')
plt.xlabel("Project Manager Experience")
plt.ylabel("Salary")
plt.show()

# Model Evaluation
y_pred=regressor.predict(x_test_scaled)
print(f"Mean Absolute Error: {mean_absolute_error(y_test,y_pred):.2f}")
print(f"Mean Squared Error: {mean_squared_error(y_test,y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test,y_pred):.2f}")

