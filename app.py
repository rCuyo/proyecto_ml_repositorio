from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
modelo = joblib.load("model.pkl")

@app.route("/")
def home():
    return "☀️ API de Predicción de Lluvias para la Región de Puno en funcionamiento"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    # Esperamos datos en formato JSON, ejemplo:
    # {"temperatura": 18.5, "humedad": 80, "presion": 1012, "viento": 12.3}

    try:
        features = np.array([[data["temperatura"], data["humedad"], data["presion"], data["viento"]]])
        prediccion = modelo.predict(features)[0]
        probabilidad = modelo.predict_proba(features)[0].tolist() if hasattr(modelo, "predict_proba") else None

        return jsonify({
            "prediccion": int(prediccion),
            "probabilidad": probabilidad
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)