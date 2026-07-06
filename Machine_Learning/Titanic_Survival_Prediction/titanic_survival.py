# Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV,cross_val_score,StratifiedKFold
from sklearn .preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

# Load Dataset from Seaborn
titanic=sns.load_dataset('titanic')
print(titanic.head(5))

# Select Relevant Features
print(titanic.count())

features=['age','pclass','sex','sibsp','parch','fare','class','who','adult_male','alone']
target='survived'

X=titanic[features]
Y=titanic[target]

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=42)

# Preprocessing
numerical_features=x_train.select_dtypes(include=['number']).columns.tolist()
categorical_features=x_train.select_dtypes(include=['object','category']).columns.tolist()

numerical_transformer=Pipeline(steps=[('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())])
categorical_transformer=Pipeline(steps=[('imputer',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore'))])

# Single Column Transformer
preprocessor=ColumnTransformer(transformers=[('num',numerical_transformer,numerical_features),('cat',categorical_transformer,categorical_features)])

# Model Pipeline
pipeline=Pipeline(steps=[('preprocessor',preprocessor),('classifier',RandomForestClassifier(random_state=42))])

# Parameter Grid
param_grid={
    'classifier__n_estimators':[50,100],
    'classifier__max_depth':[None,10,20],
    'classifier__min_samples_split':[2,5]
}

# Grid Search Cross-Validation and Fit the best model
cv=StratifiedKFold(n_splits=5,shuffle=True)

# Train the Pipeline
model=GridSearchCV(estimator=pipeline,param_grid=param_grid,cv=cv,scoring='accuracy',verbose=2)
model.fit(x_train,y_train)
print("Best Parameters:", model.best_params_)
print("Best CV Accuracy:", model.best_score_)
# Prediction & Report
y_pred=model.predict(x_test)
print("\n",classification_report(y_test,y_pred))

# Confusion Matrix and Plotting
conf_matrix=confusion_matrix(y_test,y_pred)
plt.figure()
sns.heatmap(conf_matrix,annot=True,cmap='Blues',fmt='d')
plt.title("Titanic Survival Classification Report")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()