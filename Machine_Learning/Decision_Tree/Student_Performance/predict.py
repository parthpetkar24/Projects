import joblib
import pandas as pd
import os

MODEL_PATH=os.path.dirname(os.path.abspath(__file__))
model_file=os.path.join(MODEL_PATH,"student_performance_model.pkl")
model=joblib.load(model_file)

study_hours=float(input("Enter Study Hours: "))
attendance=float(input("Enter Attendance: "))
sleep_hours=float(input("Enter Sleep Hours: "))
internet_usage=float(input("Enter Internet Usage: "))
assignments_completed=float(input("Enter Assignments Completed: "))
previous_score=float(input("Enter Previous Score: "))

user_data=pd.DataFrame({
    'study_hours':[study_hours],
    'attendance':[attendance],
    'sleep_hours':[sleep_hours],
    'internet_usage':[internet_usage],
    'assignments_completed':[assignments_completed],
    'previous_score':[previous_score]
})

prediction=model.predict(user_data)
if prediction[0]==1:
    print("\nPrediction: Placed")
else:
    print("\nPrediction: Not Placed")