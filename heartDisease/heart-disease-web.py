from flask import Flask, request, render_template
import numpy as np
from joblib import load

# Load your trained model
model = load("check_my_heart_model.joblib")

app = Flask(__name__)

@app.route('/')
def home():
    # Render an HTML form for user input
    return render_template('patient-form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from form
    try:
        data = [int(x) for x in request.form.values()]
        input_array = np.array([data])
        prediction = model.predict(input_array)
        output = "High risk of heart disease. Consult with a doctor immediately." if prediction == 1 else "Low to no risk of heart disease. If you feel any discomfort, please see a doctor"
    except Exception as e:
        output = f"Error: {e}"

    # You can modify the return to render another template with the results
    return render_template('result.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
