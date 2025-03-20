# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pickle
# import numpy as np


# # Load trained model
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)

# app = Flask(__name__)
# CORS(app)  # Allow React frontend to access API


# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.get_json()
#         if data is None:
#             return jsonify({"error": "Invalid JSON format"}), 400

#         # Dummy response (modify as per your logic)
#         return jsonify({"message": "API is working!", "received": data})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)







from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Load trained model
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model:", str(e))

app = Flask(__name__)
CORS(app)  # Allow React frontend to access API

# 🔹 Add a root route to prevent 404 errors
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask API is running!"})

# 🔹 Allow GET requests for /predict (API health check)
@app.route("/predict", methods=["GET"])
def check_api():
    return jsonify({"message": "Predict endpoint is live! Use POST request."})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("📩 Received Data:", data)  # Debugging print

        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400

        # Extract values from request (Modify based on your model's expected input)
        try:
            age = int(data.get("age", 0))  # Convert to integer
            features = np.array([[age]])  # Example: Modify according to your model input shape
        except ValueError:
            return jsonify({"error": "Invalid data format"}), 400

        # Make a prediction using the loaded model
        prediction = model.predict(features)[0]

        response = {"prediction": str(prediction)}
        print("📤 Sending Response:", response)  # Debugging print

        return jsonify(response)

    except Exception as e:
        print("❌ Error:", str(e))  # Debugging print
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
