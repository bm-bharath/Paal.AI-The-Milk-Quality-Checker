from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db
import numpy as np
import joblib
import pandas as pd
import time
from datetime import datetime
import pytz
import lightgbm

# Print LightGBM version for debugging
print(f"LightGBM version: {lightgbm.__version__}")

# Initialize Firebase
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://milk-quality-monitoring-default-rtdb.firebaseio.com/"
})

# Load trained LightGBM model
model = joblib.load("models/lightgbm_model.pkl")

# Define feature names (match the order used during training)
FEATURE_NAMES = ['pH', 'Temperature', 'Density', 'Colour']

# Define grade mapping
GRADE_MAPPING = {
    0: "The Milk is Low in Quality",
    1: "The Milk is Medium in Quality",
    2: "The Milk is High in Quality"
}

# Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/get_prediction', methods=['GET'])
def get_prediction():
    try:
        # Fetch latest sensor data from Firebase
        ref = db.reference("/milk_quality")
        data = ref.get()

        if not data:
            return jsonify({"error": "No data found in Firebase"}), 400

        # Log the raw data fetched from Firebase
        print(f"Raw data from Firebase: {data}")

        # Extract inputs with error handling, using the correct case for keys
        try:
            colour = int(float(data.get("Colour", 0)))  # Convert to int for Colour
            density = float(data.get("Density", 0))
            ph = float(data.get("pH", 0))
            temperature = float(data.get("Temperature", 0))
        except (ValueError, TypeError) as e:
            return jsonify({"error": "Invalid sensor data format"}), 400

        # Log the fetched data for debugging
        print(f"Fetched data from Firebase: Colour={colour}, Density={density}, pH={ph}, Temperature={temperature}")

        # Prepare features as DataFrame with correct column names and order
        features = pd.DataFrame(
            [[ph, temperature, density, colour]],  # Match the order of FEATURE_NAMES
            columns=FEATURE_NAMES
        )

        # Make prediction
        prediction = model.predict(features)[0]
        prediction = prediction.argmax()  # Get the class with the highest probability
        print(f"Raw model prediction: {prediction}")  # Log the raw prediction
        grade_num = int(prediction)
        grade_label = GRADE_MAPPING.get(grade_num, "Unknown")
        print(f"Mapped grade: {grade_num} -> {grade_label}")  # Log the mapped grade

        # Get current time in GMT+5:30 (IST)
        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist)
        formatted_time = current_time.strftime('%d/%m/%Y %H:%M:%S')

        # Store prediction in Firebase with formatted timestamp
        pred_ref = db.reference("/predictions")
        pred_ref.push({
            "Grade": grade_label,
            "timestamp": formatted_time
        })

        # Log the response being sent to the frontend
        response = {
            "Colour": colour,
            "Density": density,
            "pH": ph,
            "Temperature": temperature,
            "Grade": grade_label,
            "timestamp": formatted_time
        }
        print(f"Sending response to frontend: {response}")

        return jsonify(response)

    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)