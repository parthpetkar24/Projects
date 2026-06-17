import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn import metrics
import joblib
import os

MODEL_PATH=os.path.dirname(os.path.abspath(__file__))

# Data Load
path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv"
data=pd.read_csv(path)
print(data.head(5))

# Data Information
data.info()

# Encoding
sex_encoder = LabelEncoder()
bp_encoder = LabelEncoder()
chol_encoder = LabelEncoder()

data['Sex'] = sex_encoder.fit_transform(data['Sex'])
data['BP'] = bp_encoder.fit_transform(data['BP'])
data['Cholesterol'] = chol_encoder.fit_transform(data['Cholesterol'])

# Missing Values check
print(data.isnull().sum())

# Custom Map
custom_map={'drugA':0,'drugB':1,'drugC':2,'drugX':3,'drugY':4}
data["Drug_Num"]=data['Drug'].map(custom_map)

# Visualisation
sns.countplot(y="Drug",data=data)
plt.title("Drug Distribution")
plt.show()

# Correlation
print(data.drop("Drug",axis=1).corr().abs())

# Model Data Selection
x=data.drop(['Drug','Drug_Num'],axis=1)
y=data['Drug']

# Train Test Split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# Decision Tree
drugTree=DecisionTreeClassifier(criterion='entropy',max_depth=4)
drugTree.fit(x_train,y_train)

# Evaluation
tree_predict=drugTree.predict(x_test)
print("Accuracy: ",metrics.accuracy_score(y_test,tree_predict))

plot_tree(drugTree)
plt.show()

joblib.dump(drugTree,f"{MODEL_PATH}\\drug_model.pkl")
joblib.dump(sex_encoder,f"{MODEL_PATH}\\sex_encoder_model.pkl")
joblib.dump(bp_encoder,f"{MODEL_PATH}\\bp_encoder_model.pkl")
joblib.dump(chol_encoder,f"{MODEL_PATH}\\cnhol_encoder_model.pkl")

print("Model Saved Successfully")
