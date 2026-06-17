import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv("spam_or_not_spam.csv")
print(data.head(5))
print(data.describe())
print(data['label'].value_counts())

data = data.dropna(subset=["email"])

X=data['email']
Y=data['label']

vectorized=TfidfVectorizer(stop_words="english", max_features=5000)
X_vec=vectorized.fit_transform(X)


x_train,x_test,y_train,y_test=train_test_split(X_vec,Y,test_size=0.2,random_state=42)

LR=linear_model.LogisticRegression(max_iter=200)

LR.fit(x_train,y_train)

y_pred=LR.predict(x_test)
print(f"Accuracy Score: {accuracy_score(y_test,y_pred)}")