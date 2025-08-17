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
        # Redirect GET requests to the main page
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        response = {
            'message': 'Heart Attack Risk Prediction API',
            'endpoint': '/api/predict',
            'method': 'POST',
            'status': 'active'
        }
        
        self.wfile.write(json.dumps(response).encode())
    
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
