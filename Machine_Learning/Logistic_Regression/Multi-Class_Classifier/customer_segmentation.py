# Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix
from imblearn.over_sampling import SMOTE
import os

# Input the csv file
file_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(file_dir,"retail_customer_segmentation.csv")
data=pd.read_csv(file_path)
print(data.head(5))

# Exploratory Data Analysis
data=data.drop("customer_id",axis=1)

sns.countplot(y="customer_segment",data=data)
plt.title("Count per Segment")
plt.show()

print(data.info())
print(data.isnull().sum())

data=data.dropna().reset_index(drop=True)
print(data.isnull().sum())

categorical_columns=data.select_dtypes(include=["str"]).columns.to_list()
categorical_columns.remove("customer_segment")
encoder=OneHotEncoder(sparse_output=False,drop="first")
encoder_features=encoder.fit_transform(data[categorical_columns])
encoder_df=pd.DataFrame(encoder_features,columns=encoder.get_feature_names_out(categorical_columns))
encoder_data=pd.concat([data.drop(columns=categorical_columns),encoder_df],axis=1)

continous_columns=encoder_data.select_dtypes(include=["float64","int64"]).columns.to_list()
scaler=StandardScaler()
scaled_feature=scaler.fit_transform(encoder_data[continous_columns])
scaled_df=pd.DataFrame(scaled_feature,columns=scaler.get_feature_names_out(continous_columns))
prepped_data=pd.concat([encoder_data.drop(columns=continous_columns),scaled_df],axis=1)

prepped_data["customer_segment"]=prepped_data["customer_segment"].astype("category").cat.codes
print(prepped_data.head())

x=prepped_data.drop("customer_segment",axis=1)
y=prepped_data["customer_segment"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

smote = SMOTE(random_state=42)
x_train, y_train = smote.fit_resample(x_train, y_train)
print(y_train.value_counts())

LR_model_ova=OneVsRestClassifier(linear_model.LogisticRegression(class_weight='balanced',max_iter=1000))
LR_model_ova.fit(x_train,y_train)

y_pred=LR_model_ova.predict(x_test)
print(f"Accuracy= {np.round(100*accuracy_score(y_test,y_pred),2)}%")
print(f"Confusion Matrix= \n{confusion_matrix(y_test,y_pred)}")
print(f"\nF1 Score= {f1_score(y_test,y_pred,average="weighted")}")