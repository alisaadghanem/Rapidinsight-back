from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from model import DiabetesModel
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, static_folder="static")
CORS(app)

fbs_model = DiabetesModel("FBS_dataset.csv")
rbs_model = DiabetesModel("RBS_dataset.csv")
hba1c_model = DiabetesModel("HbA1c_dataset.csv")


@app.route("/")
def index():
    return send_from_directory("static/templates", "index.html")


@app.route("/css/styles.css")
def styles():
    return send_from_directory("static/css", "styles.css")


# FBS predict endpoint
@app.route("/FBS", methods=["POST"])
def predict_fbs():
    data = request.get_json()
    input_data = {
        "Age": data["age"],
        "Gender": data["gender"],
        "Polyuria": data["polyuria"],
        "Polydipsia": data["polydipsia"],
        "sudden weight loss": data["sudden weight loss"],
        "weakness": data["weakness"],
        "Polyphagia": data["polyphagia"],
        "Genital thrush": data["genital thrush"],
        "visual blurring": data["visual blurring"],
        "Itching": data["itching"],
        "Irritability": data["irritability"],
        "delayed healing": data["delayed healing"],
        "partial paresis": data["partial paresis"],
        "muscle stiffness": data["muscle stiffness"],
        "Alopecia": data["alopecia"],
        "Obesity": data["obesity"],
        "sugar_level": data["sugar_level"],
    }
    prediction = fbs_model.predict(input_data)
    return jsonify({"prediction": int(prediction[0])})


# RBS predict endpoint
@app.route("/RBS", methods=["POST"])
def predict_rbs():
    data = request.get_json()
    input_data = {
        "Age": data["age"],
        "Gender": data["gender"],
        "Polyuria": data["polyuria"],
        "Polydipsia": data["polydipsia"],
        "sudden weight loss": data["sudden weight loss"],
        "weakness": data["weakness"],
        "Polyphagia": data["polyphagia"],
        "Genital thrush": data["genital thrush"],
        "visual blurring": data["visual blurring"],
        "Itching": data["itching"],
        "Irritability": data["irritability"],
        "delayed healing": data["delayed healing"],
        "partial paresis": data["partial paresis"],
        "muscle stiffness": data["muscle stiffness"],
        "Alopecia": data["alopecia"],
        "Obesity": data["obesity"],
        "sugar_level": data["sugar_level"],
    }
    prediction = rbs_model.predict(input_data)
    return jsonify({"prediction": int(prediction[0])})


# HbA1c predict endpoint
@app.route("/HbA1c", methods=["POST"])
def predict_hba1c():
    data = request.get_json()
    input_data = {
        "Age": data["age"],
        "Gender": data["gender"],
        "Polyuria": data["polyuria"],
        "Polydipsia": data["polydipsia"],
        "sudden weight loss": data["sudden weight loss"],
        "weakness": data["weakness"],
        "Polyphagia": data["polyphagia"],
        "Genital thrush": data["genital thrush"],
        "visual blurring": data["visual blurring"],
        "Itching": data["itching"],
        "Irritability": data["irritability"],
        "delayed healing": data["delayed healing"],
        "partial paresis": data["partial paresis"],
        "muscle stiffness": data["muscle stiffness"],
        "Alopecia": data["alopecia"],
        "Obesity": data["obesity"],
        "sugar_level": data["sugar_level"],
    }
    prediction = hba1c_model.predict(input_data)
    return jsonify({"prediction": int(prediction[0])})


if __name__ == "__main__":
    app.run(debug=True)
