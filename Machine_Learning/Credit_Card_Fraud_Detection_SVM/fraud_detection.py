import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize,StandardScaler
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.svm import LinearSVC
import os

MODEL_PATH=os.path.dirname(os.path.abspath(__file__))
file=os.path.join(MODEL_PATH,'data/creditcard.csv')

data=pd.read_csv(file)
# print(data.head(5))

labels=data.Class.unique()
sizes=data.Class.value_counts().values

fig,ax=plt.subplots()
ax.pie(sizes,labels=labels,autopct="%1.3f%%")
ax.set_title("Target Variable Value Counts")
plt.show()

correlation_values=data.corr()["Class"].drop("Class")
correlation_values.plot(kind='barh',figsize=(10,6))
plt.show()

data=data.drop("Time",axis=1)
x=data.drop("Class",axis=1)
y=data["Class"]

x=StandardScaler().fit_transform(x)
x=normalize(x,norm="l1")

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

w_train=compute_sample_weight('balanced',y_train)

dt=DecisionTreeClassifier(max_depth=4,random_state=42)
dt.fit(x_train,y_train,sample_weight=w_train)

svm=LinearSVC(class_weight='balanced',random_state=41,loss='squared_hinge',fit_intercept=False,max_iter=10000)
svm.fit(x_train,y_train)

y_predict_dt=dt.predict_proba(x_test)[:,1]
print(f"Decision Tree ROC AUC Score: {roc_auc_score(y_test,y_predict_dt)}")

y_predict_svm=svm.decision_function(x_test)
print(f"SVM ROC AUC Score: {roc_auc_score(y_test,y_predict_svm)}")