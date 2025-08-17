from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'message': 'Heart Attack Risk Prediction API',
            'status': 'API is working!',
            'note': 'ML models will be added in next deployment'
        }
        
        self.wfile.write(json.dumps(response).encode())
