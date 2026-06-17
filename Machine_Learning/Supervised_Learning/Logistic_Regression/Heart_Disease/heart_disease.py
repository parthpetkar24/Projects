import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# Load the data
data="https://raw.githubusercontent.com/parthpetkar24/Projects/refs/heads/main/Machine_Learning/Logistic_Regression/Heart_Disease/data/framingham.csv"
chd_df=pd.read_csv(data)

# Pre-process the data
print(chd_df.corr())
chd_df=chd_df.drop(['currentSmoker','diaBP','prevalentHyp','diabetes'],axis=1)
chd_df = chd_df.dropna()
print(chd_df.head(5))
chd_df['TenYearCHD']=chd_df['TenYearCHD'].astype('int')

# Input Features
X=np.asarray(chd_df.drop(['TenYearCHD'],axis=1))
Y=np.asarray(chd_df['TenYearCHD'])

# Normazlize the data
X_norm=preprocessing.StandardScaler().fit(X).transform(X)

# Train and test split
x_train,x_test,y_train,y_test=train_test_split(X_norm,Y,test_size=0.4,random_state=42)

# Logistic Regression Model
LR=LogisticRegression().fit(x_train,y_train)

yhat=LR.predict(x_test)
yhat_prob=LR.predict_proba(x_test)

coefficients=pd.Series(LR.coef_[0],index=chd_df.columns[:-1])
coefficients.sort_values().plot(kind='barh')
plt.xlabel("Coefficent Value")
plt.show()

print(log_loss(y_test,yhat_prob))