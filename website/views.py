from flask import Blueprint, render_template, request

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

views = Blueprint('views', __name__)

# Charger le modèle SVM pré-entraîné
svm = joblib.load('svm_model.pkl')


# Charger le modèle de scaler pour normaliser les données
scaler = StandardScaler()

@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@views.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Charger le modèle pré-entraîné depuis le notebook
        svm = SVC()

        # Charger le modèle de scaler
        scaler = StandardScaler()

        # Charger les données entrantes depuis le formulaire HTML
        radius_mean = float(request.form['radius_mean'])
        texture_mean = float(request.form['texture_mean'])
        perimeter_mean = float(request.form['perimeter_mean'])

        # Prétraiter les données de la même manière que dans votre notebook
        input_data = [radius_mean, texture_mean, perimeter_mean, ...]

        # Normaliser les données d'entrée
        input_data = scaler.transform([input_data])

        # Effectuer la prédiction avec le modèle SVM
        prediction = svm.predict(input_data)

        # Le résultat de la prédiction est dans la variable "prediction"
        if prediction[0] == 1:
            result = "Maligne"
        else:
            result = "Bénigne"

        return f"Le diagnostic est : {result}"