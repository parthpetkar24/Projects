import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import os

def salepredict(current_temp,show_graph,show_metrices):
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(BASE_DIR,"temp_ice_cream.csv")

    data=pd.read_csv(file_path)
    # print(data)

    if show_graph=="y":
        plt.scatter(data.Temperature_C,data.IceCream_Sales,color='red')
        plt.xlabel("Temperature (in C)")
        plt.ylabel("Ice Cream Sales")
        plt.show()

    x_temp=data.Temperature_C.to_numpy()
    y_sales=data.IceCream_Sales.to_numpy()

    x_train,x_test,y_train,y_test=train_test_split(x_temp,y_sales,test_size=0.2,random_state=24)

    regressor=linear_model.LinearRegression()

    regressor.fit(x_train.reshape(-1,1),y_train)

    slope=regressor.coef_[0]
    intercept=regressor.intercept_

    if show_graph=="y":
        plt.scatter(x_train,y_train,color='red')
        x_line = np.sort(x_train)
        plt.plot(x_line,(slope*x_line)+intercept,'-b')
        plt.xlabel("Temperature (in C)")
        plt.ylabel("Ice Cream Sales")
        plt.show()

    y_pred=regressor.predict(x_test.reshape(-1,1))
    if show_metrices=="y":
        print(f"Slope= {slope}")
        print(f"Intercept= {intercept}")
        print(f"Mean Absolute Error: {mean_absolute_error(y_test,y_pred)}")
        print(f"Mean squared Error: {mean_squared_error(y_test,y_pred)}")
        print(f"R2 Score: {r2_score(y_test,y_pred)}")

    temperature=regressor.predict([[current_temp]])[0]
    return temperature

if __name__=="__main__":
    current_temp=float(input("Enter Temperature in C: "))
    see_graph=input("See Graphs? (y/n): ").lower()
    see_metrices=input("See Metrices? (y/n): ").lower()
    print(f"Predicted Sales: {salepredict(current_temp,see_graph,see_metrices)}")
