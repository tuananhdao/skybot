
# SkyBot

SkyBot is an AI-powered weather agent that gives you instant weather updates for any city.  
It follows the Google A2A (Actions-to-Actions) protocol and uses the free [Open-Meteo](https://open-meteo.com/) API.

---

## Features

- Get current temperature, weather, and wind speed for any city
- Simple A2A input/output format
- No API key needed

---

## How It Works

Send a POST request with a city name.  
SkyBot returns current weather data in a standard JSON format.

---

## Example

**Request**
```json
POST /a2a/skybot
Content-Type: application/json

{
  "city": "London"
}
```

**Response**
```json
{
  "temperature": 21.5,
  "weather_description": 3,
  "humidity": null,
  "wind_speed": 5.8,
  "unit_temperature": "°C",
  "unit_wind_speed": "km/h"
}
```

---

## Setup

1. Clone this repo:
    ```bash
    git clone https://github.com/your-username/skybot.git
    cd skybot
    ```

2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:
    ```bash
    python skybot.py
    ```

---

## API

### Endpoint

```
POST /a2a/skybot
```

### Request JSON

| Field | Type | Description               |
|-------|------|---------------------------|
| city  | text | Name of the city (e.g., "Paris") |

### Response JSON

| Field               | Type   | Description                          |
|---------------------|--------|--------------------------------------|
| temperature         | number | Current temperature                  |
| weather_description | number | Weather code (can be mapped to text) |
| humidity            | number | Humidity (%) (may be null)           |
| wind_speed          | number | Wind speed                           |
| unit_temperature    | text   | Temperature unit (°C)                |
| unit_wind_speed     | text   | Wind speed unit (km/h)               |

---

## License

MIT License

---

## Credits

- [Open-Meteo API](https://open-meteo.com/)
