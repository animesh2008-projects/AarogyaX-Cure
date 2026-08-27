import os
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

from routes.auth import auth_bp
from routes.assistant import assistant_bp
from routes.emergency import emergency_bp
from routes.hospitals import hospitals_bp
from routes.blood import blood_bp
from routes.records import records_bp
from routes.labs import labs_bp

app = Flask(__name__)
app.config.from_object(Config)

# Enable Cross-Origin Resource Sharing for frontend access
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    return response

# Register Blueprint API Routes
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(assistant_bp, url_prefix="/api/assistant")
app.register_blueprint(emergency_bp, url_prefix="/api/emergency")
app.register_blueprint(hospitals_bp, url_prefix="/api/hospitals")
app.register_blueprint(blood_bp, url_prefix="/api/blood")
app.register_blueprint(records_bp, url_prefix="/api/records")
app.register_blueprint(labs_bp, url_prefix="/api/labs")

@app.route("/")
def index():
    return jsonify({
        "name": "AarogyaX Cure Backend API",
        "version": "1.0.0",
        "status": "OPERATIONAL",
        "endpoints": {
            "health": "/api/health",
            "assistant": "/api/assistant/chat",
            "emergency_sos": "/api/emergency/sos",
            "hospitals": "/api/hospitals/nearby",
            "blood_donors": "/api/blood/donors",
            "records": "/api/records"
        }
    })

@app.route("/api/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "AarogyaX Cure Backend",
        "gemini_configured": bool(Config.GEMINI_API_KEY)
    })

if __name__ == "__main__":
    print(f"Starting AarogyaX Cure Backend on port {Config.PORT}...")
    app.run(host="0.0.0.0", port=Config.PORT, debug=Config.DEBUG)
