import numpy as np
from joblib import load
import time


model = load("check_my_heart_model.joblib")
print("ML-Based Heart Disease Prediction\n\n")

age = int(input("Enter age: "))
print("\n----------------------------------------------------------------------\n")
sex = int(input("Sex: \n'1' : male, \n'0' : female\n"))
print("\n----------------------------------------------------------------------\n")
pain = int(input("Pain type: \n'1' : Typical\n'2' : Typical Angina\n'3' : Non-Anginal\n'4' : Asymptomatic\n"))
print("\n----------------------------------------------------------------------\n")
resting_bp = int(input("Enter resting blood pressure: "))
print("\n----------------------------------------------------------------------\n")
cholesterol = int(input("Enter serum cholesterol level: "))
print("\n----------------------------------------------------------------------\n")
blood_sugar = int(input("Blood sugar level: \n'1' : above 12mg/dl during fasting \n'0' : otherwise\n"))
print("\n----------------------------------------------------------------------\n")
normal_ecf = int(input("Resting ECG level:\n'0' : Normal\n'1' : Abnormality in ST-T Wave\n'2' : Left Ventrivular Hypertrophy\n"))
print("\n----------------------------------------------------------------------\n")
max_heartRate = int(input("Enter maximum heart rate: "))
print("\n----------------------------------------------------------------------\n")
induced_angina = int(input("Has exercize induced an angina? \n'1' : Yes\n'0' : No \n"))
print("\n----------------------------------------------------------------------\n")
old_peak = int(input("ST-depression (exercise vs rest): "))
print("\n----------------------------------------------------------------------\n")
st = int(input("Enter ST segment during exercize\n'0' : Normal\n'1' : Upsloping\n'2' : Downsloping\n "))

input_array = np.array([[age, sex, pain, resting_bp, cholesterol, blood_sugar, normal_ecf, 
                        max_heartRate, induced_angina, old_peak, st]])

prediction = model.predict(input_array)

print("-------------------------------------------------------------------------")
print("RESULTS")

if prediction == 1:
    print("High risk of heart disease. Consult with a doctor immediately.")
else:
    print("Low to no risk of heart disease. If you feel any discomfort, please see a doctor")


    



