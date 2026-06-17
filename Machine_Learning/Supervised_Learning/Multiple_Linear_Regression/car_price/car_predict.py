# Imoort the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import os

# Machine Learning Model 
def car_predict(user_input):
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(BASE_DIR,"CarPrice_Assignment.csv")

    # Load Data
    df=pd.read_csv(file_path)

    # print(df.head())
    # print(df.describe())
    # Remove Categorical Data
    df=df.drop(['car_ID','symboling','CarName','fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','fuelsystem','cylindernumber','enginetype','curbweight','carheight','carwidth','carlength','wheelbase'],axis=1)

    # print(df.corr().abs())

    df=df.drop(['highwaympg'],axis=1)

    # print(df.head(9))
    
    axes=pd.plotting.scatter_matrix(df,alpha=0.2)
    for ax in axes.flatten():
        ax.xaxis.label.set_rotation(90)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha('right')
    plt.tight_layout()
    plt.gcf().subplots_adjust(wspace=0,hspace=0)
    plt.show()

    # Extract Features
    X=df.drop(['price'],axis=1).to_numpy()
    Y=df['price'].to_numpy()

    # Train and test split
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.4,random_state=42)

    # Pre-process the data
    std_scalar=preprocessing.StandardScaler()
    X_train_std=std_scalar.fit_transform(X_train)
    X_test_std=std_scalar.transform(X_test)

    # print(pd.DataFrame(X_train_std).describe().round(2))
    # print(pd.DataFrame(X_test_std).describe().round(2))

    # Build a Model
    # Multiple Linear Model object
    regressor=linear_model.LinearRegression()

    regressor.fit(X_train_std,Y_train)

    # Slopes and Intercept of the Data
    b1,b2,b3,b4,b5,b6,b7=regressor.coef_
    b0=regressor.intercept_

    # print(b1,b2,b3,b4,b5,b6,b7)
    # print(b0)

    # Visualize the Linear Model Line for each features and label
    plt.scatter(X_train_std[:,0],Y_train,color='blue')
    plt.plot(X_train_std[:,0],b0+(b1*X_train_std[:,0]))
    plt.xlabel('Engine Size')
    plt.ylabel('Price')
    plt.show()

    plt.scatter(X_train_std[:,1],Y_train,color='blue')
    plt.plot(X_train_std[:,1],b0+(b2*X_train_std[:,1]))
    plt.xlabel('Bore Ratio')
    plt.ylabel('Price')
    plt.show()

    plt.scatter(X_train_std[:,2],Y_train,color='blue')
    plt.plot(X_train_std[:,2],b0+(b3*X_train_std[:,2]))
    plt.xlabel('Stroke')
    plt.ylabel('Price')
    plt.show()

    plt.scatter(X_train_std[:,3],Y_train,color='blue')
    plt.plot(X_train_std[:,3],b0+(b4*X_train_std[:,3]))
    plt.xlabel('Compression Ratio')
    plt.ylabel('Price')
    plt.show()

    plt.scatter(X_train_std[:,4],Y_train,color='blue')
    plt.plot(X_train_std[:,4],b0+(b5*X_train_std[:,4]))
    plt.xlabel('Horespower')
    plt.ylabel('Price')
    plt.show()

    plt.scatter(X_train_std[:,5],Y_train,color='blue')
    plt.plot(X_train_std[:,5],b0+(b6*X_train_std[:,5]))
    plt.xlabel('Peak RPM')
    plt.ylabel('Price')
    plt.show()

    plt.scatter(X_train_std[:,6],Y_train,color='blue')
    plt.plot(X_train_std[:,6],b0+(b7*X_train_std[:,6]))
    plt.xlabel('City MPG')
    plt.ylabel('Price')
    plt.show()

    # Model Evaluation
    y_pred=regressor.predict(X_test_std)
    print(f"Mean Absolute Error: {mean_absolute_error(Y_test,y_pred):.2f}")
    print(f"Mean Squared Error: {mean_squared_error(Y_test,y_pred):.2f}")
    print(f"R2 Score: {r2_score(Y_test,y_pred):.2f}")

    # User Input Prediction
    user_input=std_scalar.fit_transform(user_input)
    user_input_predict=regressor.predict(user_input)
    return user_input_predict[0]

# Main Function
if __name__=="__main__":

    # Take User input
    print("Enter Car Details: ")

    enginesize = float(input("Engine Size: "))
    boreratio = float(input("Bore Ratio: "))
    stroke = float(input("Stroke: "))
    compressionratio = float(input("Compression Ratio: "))
    horsepower = float(input("Horsepower: "))
    peakrpm = float(input("Peak RPM: "))
    citympg = float(input("City MPG: "))

    # Merge the user input as a numpy array
    user_input=np.array([[enginesize, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg]])

    # Predict the Car Price
    print(f"Predicted Price : {car_predict(user_input):.2f}")