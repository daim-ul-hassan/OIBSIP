import os 
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    print("Error: OPENWEATHER_API_KEY is not configured.")
    exit()

print("Weather App")

location = input("Enter city name or ZIP code: ").strip()

if not location:
    print("Error: Please enter a city name or ZIP code.")
    exit()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": location,
    "appid": api_key,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 401:
        print("Error: Invalid API Key.")
        exit(0)

    if response.status_code == 404:
        print("Error: City not found.")
        exit()

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Error: The weather request timed out.")
    exit()

except requests.exceptions.RequestException:
    print("Error: Could not connect to the weather service.")
    exit()

data = response.json()

temperature_c = data["main"]["temp"]
humidity = data["main"]["humidity"]
condition = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]

temperature_f = (temperature_c * 9/5) + 32

print("\nWeather for:",location)
print("Temperature:",round(temperature_c,2), "°C")
print("Temperature:",round(temperature_f,2), "°F")
print("Humidity:",humidity,"%")
print("Condition:",condition.title())
print("Wind Speed:",wind_speed,"m/s")