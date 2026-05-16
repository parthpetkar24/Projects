# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix
import joblib
import os

# File Path
MODEL_PATH=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(MODEL_PATH,"student_dataset_10000_rows.csv")

# Read Data
data=pd.read_csv(file_path)
# print(data.head(5))

# EDA
sns.countplot(y="placement_status",data=data)
plt.title("Placement Status Distribution")
plt.show()

print(data.isnull().sum())

print(data.info())

# Custom Mapping
custom_map={"Not Placed":0,"Placed":1}
data['placement_status_map']=data['placement_status'].map(custom_map)

# Check Correlation 
print(data.drop("placement_status",axis=1).corr().abs())

# Training and Testing Data
x=data.drop(['placement_status','placement_status_map','exam_score'],axis=1)
y=data['placement_status_map']

# Model Data Selection
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

# Decision Tree Model
performanceTree=DecisionTreeClassifier(criterion='entropy',max_depth=4)
performanceTree.fit(x_train,y_train)

# Model Evaluation
performancePredict=performanceTree.predict(x_test)
print("Accuracy: ",accuracy_score(y_test,performancePredict))
print("\n Confusion Matrix:\n",confusion_matrix(y_test,performancePredict))
print("\n Classification Report:\n",classification_report(y_test,performancePredict))

# Tree Plotting
plt.figure(figsize=(20,10))
plot_tree( performanceTree, feature_names=x.columns,class_names=['Not Placed','Placed'],filled=True)
plt.show()

# Saving Model
model_file=os.path.join(MODEL_PATH,"student_performance_model.pkl")
joblib.dump(performanceTree,model_file)
print("Model Saved Successfully")