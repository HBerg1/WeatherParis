from flask import request, Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import json
import redis
import os
import requests

load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')
if api_key is None:
    raise ValueError("API key not found. Please set WEATHER_API_KEY in your .env file.")

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

redis = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello():
	return "Hello World!"
	
@app.route('/api/test', methods=['GET'])
def test():

    user_id = request.args.get('userId')
    search = request.args.get('search')
    return jsonify({"message": "test!", "user_id": user_id})

@app.route('/api/forecast', methods=['GET'])
def forecast():
    api_arg = request.args.get('arg', 'Paris')
    refresh = request.args.get('refresh', False)

    api_url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={api_arg}&days=10&aqi=no&alerts=no"

    cached_data = redis.get(api_url)
    if not refresh and cached_data:
        return jsonify(json.loads(cached_data))
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            redis.setex(api_url, 300, json.dumps(data))
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to fetch data"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=8000)