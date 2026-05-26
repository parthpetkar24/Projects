import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error,r2_score
import time

# Load California housing dataset
data=pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/UZPRFNucrENAFm25csq6eQ/California-housing.csv')
print(data.head(5))

print(data.info())
print(data.describe())
print(data.isnull().sum())

x=data.drop('Target',axis=1)
y=data['Target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)  

# Models
n_estimators=100
rf=RandomForestRegressor(n_estimators=n_estimators,random_state=42)
xgb=XGBRegressor(n_estimators=n_estimators,random_state=42)

# Train and evaluate Random Forest
# RandomForest 
start_time=time.time()
rf.fit(x_train,y_train)
end_time=time.time()
rf_train_time=end_time-start_time

# XGBoost
start_time=time.time()
xgb.fit(x_train,y_train)
end_time=time.time()
xgb_train_time=end_time-start_time

# Evaluate
start_time=time.time()
rf_pred=rf.predict(x_test)  
end_time=time.time()
rf_pred_time=end_time-start_time

start_time=time.time()
xgb_pred=xgb.predict(x_test)           
end_time=time.time()
xgb_pred_time=end_time-start_time

print(f"Random Forest:\nMSE:{mean_squared_error(y_test,rf_pred):.4f}, R2: {r2_score(y_test,rf_pred):.4f}")
print(f"XGBoost:\nMSE:{mean_squared_error(y_test,xgb_pred):.4f}, R2: {r2_score(y_test,xgb_pred):.4f}")

# Time taken
print(f"Random Forest Training Time: {rf_train_time:.4f} seconds, Prediction Time: {rf_pred_time:.4f} seconds")
print(f"XGBoost Training Time: {xgb_train_time:.4f} seconds, Prediction Time: {xgb_pred_time:.4f} seconds")