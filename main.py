from flask import Flask, request
from api_client import build_weather_query,build_forecast_query, get_weather_data, get_forecast_data

app = Flask(__name__)

@app.route('/get-weather-data', methods=['POST'])
def display_weather_info():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.get_json()
        city_input = json_data["city"]
        measurement_unit = json_data["measurement_unit"]

        url = build_weather_query(city_input, measurement_unit)
        weather_data = get_weather_data(url)

        return weather_data

@app.route('/get-forecast-data', methods=['POST'])
def display_forecast_info():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json_data = request.get_json()
        city_input = json_data["city"]
        measurement_unit = json_data["measurement_unit"]

    url = build_forecast_query(city_input, measurement_unit)
    forecast_data = get_forecast_data(url)

    return forecast_data


if __name__ == '__main__':
    app.run(debug=True)