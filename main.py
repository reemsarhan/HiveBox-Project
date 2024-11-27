from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

APP_VERSION = "v0.0.1"

@app.route("/version", methods=["GET"])
def get_version():
    return f"Current App Version: {APP_VERSION}"

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data),201

# Mock data for senseBox readings
sensebox_data = [
    {"timestamp": datetime.now() - timedelta(minutes=30), "temperature": 25.5},
    {"timestamp": datetime.now() - timedelta(minutes=45), "temperature": 26.0},
    {"timestamp": datetime.now() - timedelta(hours=2), "temperature": 27.0},  # Excluded
]

@app.route("/temperature", methods=["GET"])
def get_temperature():
    one_hour_ago = datetime.now() - timedelta(hours=1)
    
    # Filter data to include only readings from the last hour
    recent_data = [d["temperature"] for d in sensebox_data if d["timestamp"] >= one_hour_ago]
    
    if not recent_data:
        return jsonify({"error": "No recent temperature data available"}), 404

    # Calculate the average temperature
    average_temp = sum(recent_data) / len(recent_data)
    return jsonify({"average_temperature": round(average_temp, 2)})

if __name__ == "__main__":
    app.run(debug=True)
