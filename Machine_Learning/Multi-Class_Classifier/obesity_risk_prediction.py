import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import accuracy_score

file_path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/GkDzb7bWrtvGXdPOfk6CIg/Obesity-level-prediction-dataset.csv"
data=pd.read_csv(file_path)
print(data.head(5))

sns.countplot(y='NObeyesdad',data=data)
plt.title('Distribution of Obesity Levels')
plt.show()

continous_columns=data.select_dtypes(include=['float64']).columns.tolist()

scaler=StandardScaler()
scaled_feature=scaler.fit_transform(data[continous_columns])
scaled_df=pd.DataFrame(scaled_feature,columns=scaler.get_feature_names_out(continous_columns))
scaled_data=pd.concat([data.drop(columns=continous_columns),scaled_df],axis=1)

categorical_columns=scaled_data.select_dtypes(include=['object','string','category']).columns.tolist()
categorical_columns.remove('NObeyesdad')

encoder=OneHotEncoder(sparse_output=False,drop='first')
encoded_feature=encoder.fit_transform(scaled_data[categorical_columns])

encoded_df=pd.DataFrame(encoded_feature,columns=encoder.get_feature_names_out(categorical_columns))
prepped_data=pd.concat([scaled_data.drop(columns=categorical_columns),encoded_df],axis=1)

prepped_data['NObeyesdad'].astype('category').cat.codes
print(prepped_data.head(5))

X=prepped_data.drop('NObeyesdad',axis=1)
y=prepped_data['NObeyesdad']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

model_ovo=OneVsOneClassifier(LogisticRegression(max_iter=1000))
model_ovo.fit(X_train,y_train)

y_pred=model_ovo.predict(X_test)
print(f"Accuracy= {np.round(100*accuracy_score(y_test,y_pred),2)} %")