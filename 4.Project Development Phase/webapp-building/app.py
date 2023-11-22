import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('rdf.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=["POST", "GET"])
def predict():
    return render_template("input.html")

@app.route('/submit', methods=["POST", "GET"])
def submit():
    input_features = [int(x) for x in request.form.values()]
    input_features = [np.array(input_features)]
    names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome',
             'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    data = pd.DataFrame(input_features, columns=names)

    prediction = model.predict(data)
    prediction = int(prediction)

    if prediction == 1:
        return render_template("not_approved.html")
    else:
        return render_template("approved.html")

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
