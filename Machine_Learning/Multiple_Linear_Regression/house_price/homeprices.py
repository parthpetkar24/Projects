import pandas as pd
import numpy as np
import matplotlib.pyplot
import math
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler
import os

def homepricepredict(area,bedroom,age):
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(BASE_DIR,"homeprices.csv")

    data=pd.read_csv(file_path)
    # print(data)

    median_bedrooms=math.floor(data.bedrooms.median())
    data.bedrooms=data.bedrooms.fillna(median_bedrooms)
    newdata=data.copy()
    # print(newdata)

    X=newdata[['area','bedrooms','age']]
    Y=newdata['price']

    scaler=StandardScaler()
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=42)

    x_train_scaled=scaler.fit_transform(x_train)
    x_test_scaled=scaler.transform(x_test)

    regressor=linear_model.LinearRegression()
    regressor.fit(x_train_scaled,y_train)
    b0= regressor.intercept_
    b1,b2,b3=regressor.coef_

    y_pred=regressor.predict(x_test_scaled)
    print(f"MAE: {mean_absolute_error(y_test,y_pred)}")
    print(f"MSE: {mean_squared_error(y_test,y_pred)}")
    print(f"R2 Score: {r2_score(y_test,y_pred)}")

    conditions=pd.DataFrame([[area,bedroom,age]],columns=['area','bedrooms','age'])
    conditions=scaler.transform(conditions)
    predict_price=regressor.predict(conditions)[0]
    return predict_price

if __name__=="__main__":
    area=int(input("Enter Area in sq. ft. : "))
    bedroom=int(input("Enter Number of Bedrooms: "))
    age=int(input("Enter Age of House: "))
    print(f"Predicted House Price= {homepricepredict(area,bedroom,age)}")