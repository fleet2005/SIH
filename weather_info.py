import requests

def get_weather_data(latitude, longitude, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        weather_data = {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather_description": data["weather"][0]["description"]
        }
        
        return weather_data
    else:
        return {"error": "Failed to fetch data. Please check the coordinates and API key."}


latitude = 28.6139
longitude = 77.2090
api_key = "e7aec3756ac4a43c76865553fea16745"

weather_data = get_weather_data(latitude, longitude, api_key)
print(weather_data)
