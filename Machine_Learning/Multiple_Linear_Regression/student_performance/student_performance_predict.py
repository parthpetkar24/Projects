# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import os

# Fucntion to Predict the Student Performance
def student_performance_predict(user_data):
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(BASE_DIR,"Student_Performance.csv")

    stu_data=pd.read_csv(file_path)

    # print(stu_data.head(5))

    stu_data=stu_data.drop(['Extracurricular Activities'],axis=1)

    # print(stu_data.head(5))

    print(stu_data.corr().abs())

    stu_data=stu_data.drop(['Sleep Hours','Sample Question Papers Practiced'],axis=1)
    print(stu_data.head(5))

    # axes=pd.plotting.scatter_matrix(stu_data,alpha=0.2)
    # for ax in axes.flatten():
    #     ax.xaxis.label.set_rotation(90)
    #     ax.yaxis.label.set_rotation(0)
    #     ax.yaxis.label.set_ha('right')
    # plt.tight_layout()
    # plt.gcf().subplots_adjust(wspace=0,hspace=0)
    # plt.show()

    X = stu_data[['Hours Studied', 'Previous Scores']].values
    Y = stu_data['Performance Index'].values

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.4,random_state=42)

    std_scaler=preprocessing.StandardScaler()
    X_train_std=std_scaler.fit_transform(X_train)
    X_test_std=std_scaler.transform(X_test)

    regressor=linear_model.LinearRegression()

    regressor.fit(X_train_std,Y_train)

    b0=regressor.intercept_
    b1,b2=regressor.coef_

    # plt.scatter(X_train_std[:,0],Y_train)
    # plt.plot(X_train_std[:,0],b0+(b1*X_train_std[:,0]),'-g')
    # plt.xlabel('Hours Studied')
    # plt.ylabel('Performance')
    # plt.show()

    # plt.scatter(X_train_std[:,1],Y_train)
    # plt.plot(X_train_std[:,1],b0+(b2*X_train_std[:,1]),'-g')
    # plt.xlabel('Previous Score')
    # plt.ylabel('Performance')
    # plt.show()

    y_pred=regressor.predict(X_test_std)
    print(f"Mean absolute error: {mean_absolute_error(Y_test,y_pred):.2f}")
    print(f"Mean squared error: {mean_squared_error(Y_test,y_pred):.2f}")
    print(f"R2 Score: {r2_score(Y_test,y_pred):.2f}")

    user_data=std_scaler.transform(user_data)
    user_score_predict=regressor.predict(user_data)
    return user_score_predict[0]


if __name__=="__main__":
    hours_studied=float(input("Enter Number of Hours Studied: "))
    previous_score=float(input("Enter Previous Score: "))
    user_data=np.array([[hours_studied,previous_score]])
    print(f"Predicted Score for next test: {student_performance_predict(user_data):.2f}")