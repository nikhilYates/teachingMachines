from flask import Flask, request, render_template, redirect, session
import numpy as np
from joblib import load

# Load your trained model
model = load("check_my_heart_model.joblib")


app = Flask(__name__)

app.config['SECRET_KEY'] = 'h34rt_pr3dict10n_4lg0'

@app.route('/')
def home():
    return render_template('patient-form.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    # Retrieve data from form
    try:
        if request.method == "POST":
            age = int(request.form["age"])
            sex = int(request.form["sex"])
            rbp = int(request.form["r-bp"])
            chol = int(request.form["chol"])
            pain_type = int(request.form["angina"])
            bs = int(request.form["b-sugar"])
            r_ecg = int(request.form["rest-ecg"])
            mbp = int(request.form["m-bp"])
            ex_angina = int(request.form["ex-angina"])
            st_diff = float(request.form["st-dep"])
            st_slope = float(request.form["st-seg"])
            # print(list[data])
            input_array = np.array([[age, sex, pain_type, rbp, chol, bs, r_ecg, mbp, ex_angina, st_diff, st_slope]])
            prediction = model.predict(input_array)
            output = "High risk of heart disease. Consult with a doctor immediately." if prediction == 1 else "Low to no risk of heart disease. If you feel any discomfort, please see a doctor"
            session['output'] = output
            return redirect("/prediction", code=302)
        else:
            return render_template('patient-form.html')
    except Exception as e:
        output = f"Error: {e}"
        return f"Error: {e}"
        

@app.route('/prediction', methods=["GET"])
def output_message():
    return f"<h1>{session.get('output')}</h1>"

if __name__ == "__main__":
    app.run()
