from flask import Flask, request, jsonify
from flask_cors import CORS

from database import create_database, save_user
from hackathon import analyze_symptoms

app = Flask(__name__)
CORS(app)

# Create database
create_database()


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "HealthGuard AI Backend is running!"
    })


@app.route("/api/symptoms", methods=["POST"])
def symptoms():

    data = request.get_json(silent=True) or {}

    age = data.get("age")
    symptom = data.get("symptom")

    if age is None or not symptom:
        return jsonify({
            "error": "Age and symptoms are required"
        }), 400

    try:
        age = int(age)
        if age < 1 or age > 120:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({
            "error": "Please enter a valid age"
        }), 400

   

    result = analyze_symptoms(age, symptom)

    return jsonify({
        "age": age,
        "symptoms": symptom,
        "status": result["status"],
        "message": result["message"]
    })


@app.route("/save", methods=["POST"])
def save():

    data = request.get_json(silent=True) or {}

    age = data.get("age")
    symptoms = data.get("symptoms")

    if age is None or not symptoms:
        return jsonify({
            "error": "Age and symptoms are required"
        }), 400

    try:
        age = int(age)
        if age < 1 or age > 120:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({
            "error": "Invalid age"
        }), 400


    save_user(age, symptoms)

    return jsonify({
        "message": "User data saved successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)