from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Helper function to get latitude and longitude for a city
def get_lat_lon(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    r = requests.get(url)
    data = r.json()
    if data.get("results"):
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
        return lat, lon
    return None, None

# Main A2A Skill Endpoint
@app.route("/a2a/skybot", methods=["POST"])
def skybot():
    # Input should be JSON with 'city' field
    data = request.json
    city = data.get("city")
    if not city:
        return jsonify({"error": "Missing city"}), 400

    # Get latitude and longitude
    lat, lon = get_lat_lon(city)
    if lat is None or lon is None:
        return jsonify({"error": "City not found"}), 404

    # Get current weather
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current_weather=true"
    )
    r = requests.get(weather_url)
    weather = r.json().get("current_weather", {})

    # Prepare A2A response
    response = {
        "temperature": weather.get("temperature"),
        "weather_description": weather.get("weathercode"),  # Needs code to text mapping
        "humidity": None,  # Open-Meteo does not provide humidity in this endpoint
        "wind_speed": weather.get("windspeed"),
        "unit_temperature": "°C",
        "unit_wind_speed": "km/h",
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5000)
