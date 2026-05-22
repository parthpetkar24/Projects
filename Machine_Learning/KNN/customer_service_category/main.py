import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv")
print(data.head(5))

print(data['custcat'].value_counts())

correlation_matrix=data.corr()
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.show()

correlation_values=abs(data.corr()['custcat'].drop('custcat')).sort_values(ascending=False)
print(correlation_values)

x=data.drop("custcat",axis=1)
y=data["custcat"]

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

Ks=50
acc=np.zeros((Ks))
std_acc=np.zeros((Ks))
for n in range(1,Ks+1):
    knn_model_n=KNeighborsClassifier(n_neighbors=n,weights='distance').fit(x_train,y_train)
    yhat=knn_model_n.predict(x_test)
    acc[n-1]=accuracy_score(y_test,yhat)
    std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])

plt.plot(range(1,Ks+1),acc,'g')
plt.fill_between(range(1,Ks+1),acc-1*std_acc,acc+1*std_acc,alpha=0.10)
plt.legend(('Accuracy_value','Standard_Deviation'))
plt.ylabel('Model_Accuracy')
plt.xlabel('Number of Neighbours(k)')
plt.tight_layout()
plt.show()

k=acc.argmax()+1
best_accuracy=acc.max()

print(f"k= {k}\nAccuracy= {best_accuracy}")