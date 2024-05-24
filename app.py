from flask import Flask, jsonify, render_template
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Get the OpenWeatherMap API key from the environment variable
API_KEY = "0e1de83f6c6ac5af1548b8965bc968af"

def get_weather_data(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or data.get("cod") != 200:
        print(f"Error fetching weather data: {data.get('message', 'Unknown error')}")
        return None
    return data

airports = [
    {"name": "JFK", "lat": 40.6413, "lon": -73.7781},
    {"name": "LAX", "lat": 33.9416, "lon": -118.4085},
    {"name": "ORD", "lat": 41.9742, "lon": -87.9073},
    {"name": "ATL", "lat": 33.6407, "lon": -84.4277},
    {"name": "DFW", "lat": 32.8998, "lon": -97.0403},
    {"name": "LHR", "lat": 51.4700, "lon": -0.4543},
    {"name": "DXB", "lat": 25.2532, "lon": 55.3657},
    {"name": "HND", "lat": 35.5494, "lon": 139.7798},
    {"name": "HKG", "lat": 22.3080, "lon": 113.9185},
    {"name": "CDG", "lat": 49.0097, "lon": 2.5479},
    {"name": "SIN", "lat": 1.3644, "lon": 103.9915},
    {"name": "FRA", "lat": 50.0379, "lon": 8.5622},
    {"name": "AMS", "lat": 52.3105, "lon": 4.7683},
    {"name": "SYD", "lat": -33.9399, "lon": 151.1753},
    {"name": "ICN", "lat": 37.4602, "lon": 126.4407},
    {"name": "PVG", "lat": 31.1443, "lon": 121.8083},
    {"name": "PEK", "lat": 40.0799, "lon": 116.6031},
    {"name": "YYZ", "lat": 43.6777, "lon": -79.6248},
    {"name": "GRU", "lat": -23.4356, "lon": -46.4731},
    {"name": "MEX", "lat": 19.4363, "lon": -99.0721},
    {"name": "SEA", "lat": 47.4502, "lon": -122.3088},
    {"name": "MIA", "lat": 25.7959, "lon": -80.2870},
    {"name": "MUC", "lat": 48.3538, "lon": 11.7861},
    {"name": "EZE", "lat": -34.8222, "lon": -58.5358},
    {"name": "BOM", "lat": 19.0896, "lon": 72.8656},
    {"name": "SFO", "lat": 37.6213, "lon": -122.3790},
    {"name": "BCN", "lat": 41.2974, "lon": 2.0833},
    {"name": "MAD", "lat": 40.4983, "lon": -3.5676},
    {"name": "JNB", "lat": -26.1367, "lon": 28.2410},
    {"name": "DME", "lat": 55.4146, "lon": 37.8995},
]

#just a test
@app.route('/weather', methods=['GET'])
def get_weather():
    weather_data = []
    for airport in airports:
        data = get_weather_data(API_KEY, airport["lat"], airport["lon"])
        if data:
            weather_features = {
                "DEST": airport["name"],
                "timestamp": datetime.now().isoformat(),
                "temperature": data.get('main', {}).get('temp', None),
                "wind_speed": data.get('wind', {}).get('speed', None),
                "wind_direction": data.get('wind', {}).get('deg', None),
                "visibility": data.get('visibility', None),
                "humidity": data.get('main', {}).get('humidity', None),
                "pressure": data.get('main', {}).get('pressure', None),
                "cloud_cover": data.get('clouds', {}).get('all', None),
            }
            weather_data.append(weather_features)
    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True, port=1234)
