import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import OneHotEncoder,normalize
import os

MODEL_PATH=os.path.dirname(os.path.abspath(__file__))
file=os.path.join(MODEL_PATH,"cardekho_data.csv")

data=pd.read_csv(file)
print(data.head(5))

print(data.info())
print(data.isnull().sum())

categorical_features=data.select_dtypes(include='str').columns.to_list()
encoded=OneHotEncoder(sparse_output=False,drop='first')
encoded_features=encoded.fit_transform(data[categorical_features])
encoded_df=pd.DataFrame(encoded_features,columns=encoded.get_feature_names_out(categorical_features))
encoded_data=pd.concat([data.drop(columns=categorical_features),encoded_df],axis=1)
# print(encoded_data.head(5))

print(encoded_data.corr().abs())

x=encoded_data.drop("Selling_Price",axis=1)
y=encoded_data[['Selling_Price']]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

dt_reg=DecisionTreeRegressor(criterion='squared_error',max_depth=4,random_state=42)
dt_reg.fit(x_train,y_train)

y_pred=dt_reg.predict(x_test)
print(f"MSE: {mean_squared_error(y_test,y_pred)}")
print(f"R2 Score: {r2_score(y_test,y_pred)}")