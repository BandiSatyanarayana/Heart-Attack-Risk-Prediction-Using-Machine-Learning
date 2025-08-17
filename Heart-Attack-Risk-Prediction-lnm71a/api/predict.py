from http.server import BaseHTTPRequestHandler
import json
import numpy as np
import joblib
import os
from urllib.parse import parse_qs, urlparse

# Load models (these will be cached between invocations)
def load_models():
    try:
        # Load scaler
        scaler = joblib.load('models/scaler.pkl')
        
        # Load features
        with open('models/features.json', 'r') as f:
            features = json.load(f)
        
        # Load models
        models = {
            'knn': ('K-Nearest Neighbors', joblib.load('models/knn_model.pkl')),
            'logreg': ('Logistic Regression', joblib.load('models/logreg_model.pkl'))
        }
        
        return scaler, features, models
    except Exception as e:
        return None, None, None

# Global variables for caching
scaler, features, models = load_models()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML form
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heart Disease Risk Predictor using Machine Learning</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 40px;
            max-width: 700px;
            margin: auto;
            background-color: #f2f6f9;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        form {
            background-color: #fff;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
        }
        label {
            font-weight: bold;
            display: block;
            margin-top: 15px;
        }
        input[type="text"],
        input[type="number"],
        select,
        button {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #007bff;
            color: white;
            font-weight: bold;
            margin-top: 20px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 25px;
            padding: 15px;
            background-color: #eaf7ea;
            border-left: 5px solid #4CAF50;
            font-size: 16px;
        }
        .error {
            background-color: #fbeaea;
            border-left: 5px solid #f44336;
        }
    </style>
</head>
<body>
    <h2>Heart Disease Risk Predictor using Machine Learning</h2>
    <form id="predictionForm">
        <label for="name">Your Name</label>
        <input type="text" name="name" required placeholder="Enter your name">

        <label for="age">Age (32 - 70)</label>
        <input type="number" name="age" min="32" max="70" step="1" required>

        <label for="totChol">Total Cholesterol (107 - 696)</label>
        <input type="number" name="totChol" min="107" max="696" step="1" required>

        <label for="sysBP">Systolic Blood Pressure (83 - 295)</label>
        <input type="number" name="sysBP" min="83" max="295" step="1" required>

        <label for="diaBP">Diastolic Blood Pressure (48 - 142)</label>
        <input type="number" name="diaBP" min="48" max="142" step="1" required>

        <label for="BMI">BMI (15.54 - 56.8)</label>
        <input type="number" name="BMI" min="15.54" max="56.8" step="0.01" required>

        <label for="heartRate">Heart Rate (44 - 143)</label>
        <input type="number" name="heartRate" min="44" max="143" step="1" required>

        <label for="glucose">Glucose (40 - 394)</label>
        <input type="number" name="glucose" min="40" max="394" step="1" required>

        <label for="model">Select Model</label>
        <select name="model" required>
            <option value="knn">K-Nearest Neighbors</option>
            <option value="logreg">Logistic Regression</option>
        </select>

        <button type="submit">Predict</button>
    </form>

    <div id="result"></div>

    <script>
        document.getElementById('predictionForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/api/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                const resultDiv = document.getElementById('result');
                if (result.error) {
                    resultDiv.className = 'result error';
                    resultDiv.innerHTML = '<strong>Error:</strong> ' + result.error;
                } else {
                    resultDiv.className = 'result';
                    resultDiv.innerHTML = `
                        <strong>Prediction:</strong> ${result.prediction}<br>
                        <strong>Confidence:</strong> ${result.confidence}
                    `;
                }
            } catch (error) {
                const resultDiv = document.getElementById('result');
                resultDiv.className = 'result error';
                resultDiv.innerHTML = '<strong>Error:</strong> Failed to get prediction';
            }
        });
    </script>
</body>
</html>
        """
        
        self.wfile.write(html_content.encode())
    
    def do_POST(self):
        # Handle prediction requests
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
            
            # Extract form data
            name = data.get('name', 'User').strip()
            age = float(data.get('age', 0))
            totChol = float(data.get('totChol', 0))
            sysBP = float(data.get('sysBP', 0))
            diaBP = float(data.get('diaBP', 0))
            bmi = float(data.get('BMI', 0))
            heartRate = float(data.get('heartRate', 0))
            glucose = float(data.get('glucose', 0))
            model_key = data.get('model', 'knn')
            
            # Validate model selection
            if model_key not in models:
                raise ValueError("Invalid model selected")
            
            # Prepare input for prediction
            input_values = [age, totChol, sysBP, diaBP, bmi, heartRate, glucose]
            input_array = np.array(input_values).reshape(1, -1)
            input_scaled = scaler.transform(input_array)
            
            # Get prediction
            model_name, model = models[model_key]
            pred = model.predict(input_scaled)[0]
            prob = model.predict_proba(input_scaled)[0][pred]
            
            # Prepare response
            if pred == 0:
                prediction = f"{name}, you are safe. 😊 (Model: {model_name})"
            else:
                prediction = f"{name}, you are at risk. 👽 (Model: {model_name})"
            
            confidence = f"{prob * 100:.2f}%"
            
            response = {
                'prediction': prediction,
                'confidence': confidence,
                'model': model_name
            }
            
        except Exception as e:
            response = {
                'error': str(e)
            }
        
        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        # Handle CORS preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
