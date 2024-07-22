import requests
import json 
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather_data(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url= url)
    data = response.json()
    return data

if __name__ == "__main__":
    api_key = os.getenv('OPENWEATHER_API_KEY')
    # Add your lat and lon
    lat = ''
    lon = ''
    weather_data = get_weather_data(api_key, lat,lon)

    os.makedirs('data',exist_ok= True)
    with open('data/weather.json','w') as f:
        json.dump(weather_data, f)
