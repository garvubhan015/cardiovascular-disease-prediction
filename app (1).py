from flask import Flask, render_template, request
import pickle
import numpy as np
from datetime import datetime

app = Flask(__name__)


model = pickle.load(open("model.pkl", "rb"))


def calculate_age_in_days(birthdate):
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')

    current_date = datetime.now()

    age_in_days = (current_date - birthdate).days

    return age_in_days



@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        fn=request.form["first"]
        ln=request.form["last"]
        age = request.form["age"]
        gender = request.form["gender"]
        height = request.form["height"]
        weight = request.form["weight"]
        ap_hi = request.form["ap_hi"]
        ap_lo = request.form["ap_lo"]
        cholesterol = request.form["cholesterol"]
        glucose = request.form["glucose"]
        active = request.form["active"]
        height = float(height)
        weight = float(weight)
        ap_hi = float(ap_hi)
        ap_lo = float(ap_lo)
        age=calculate_age_in_days(age)
        cholesterol=int(cholesterol)
        glucose=int(glucose)

        if(active=="yes"):
            active=1
        else:
            active=0    
#----------------------------------------------------------------------------------------------------------#             
        if(gender=="male"):
            gender=1
        else:
            gender=0
#----------------------------------------------------------------------------------------------------------#            

        
        
      	
        prediction = model.predict(
            [[age, gender, height, weight, ap_hi, ap_lo, cholesterol, glucose, active]])
        if (prediction[0] == 1):
            return "<html><body style='background-image: linear-gradient(45deg, #71b7e6, #9B59B5);'><div style='padding-top:220px; justify-content:center; display:grid;'><h1 style='justify-content:center; display:flex; '>"+fn+" "+ln+" has a high possibility of Cardiovascular Disease</h1><a style='justify-content:center; display:flex;' href='/'><button style='font-size:25px; border-radius:6px;'>Return</button ></a></div></body></html>"
        else:
            return "<html><body style='background-image: linear-gradient(45deg, #71b7e6, #9B59B5);'><div style='padding-top:220px; ustify-content:center; display:grid;'><h1 style='justify-content:center; display:flex; '>"+fn+" "+ln+" does not have Cardiovascular Disease</h1><a style='justify-content:center; display:flex;' href='/'><button style='font-size:25px; border-radius:6px;'>Return</button></a></div></body></html>"


if __name__ == '__main__':
    app.run(debug=True)
