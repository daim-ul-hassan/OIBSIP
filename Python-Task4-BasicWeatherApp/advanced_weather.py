import tkinter as tk
import os 
import requests
from dotenv import load_dotenv
from PIL import Image,ImageTk
from io import BytesIO

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

unit = "metric"

root = tk.Tk()

root.title("Weather App")
root.geometry("700x1000")

title = tk.Label(
    root,
    text="Weather App",
    font = ("Arial",18,"bold")
)

title.pack(pady=20)

location_label = tk.Label(
    root,
    text = "Entry City or ZIP Code: "
)

location_label.pack(pady=(20,5))

location_entry = tk.Entry(
    root,
    width = 25
)

location_entry.pack()

icon_display = tk.Label(
    root
)

icon_display.pack(pady=10)

forecast_var = tk.StringVar()

forecast_display = tk.Label(
    root,
    textvariable = forecast_var,
    font = ("Arial", 10),
    justify = "left"
)

forecast_display.pack(pady=10)

daily_forecast_var = tk.StringVar()

daily_forecast_display = tk.Label(
    root,
    textvariable=daily_forecast_var,
    font=("Arial",10),
    justify="left"
)

daily_forecast_display.pack(pady=10)


result_var = tk.StringVar()

result_display = tk.Label(
    root,
    textvariable = result_var,
    font = ("Arial",12),
    justify = "left"
)

result_display.pack(pady=20)

def get_weather():

    icon_display.config(image="")
    icon_display.image = None

    if not api_key:
        result_var.set("Error: API key is not configured.")
        result_display.config(fg="red")
        return

    location = location_entry.get().strip()

    if not location:
        result_var.set("Error: Please enter a city name or ZIP code.")
        result_display.config(fg="red")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": unit
    }

    try:
        response = requests.get(
        url, 
        params=params, 
        timeout=10
        )

        if response.status_code == 401:
            result_var.set("Error: Invalid API key.")
            result_display.config(fg="red")
            return

        if response.status_code == 404:
            result_var.set("Error: City not found.")
            result_display.config(fg="red")
            return

        if response.status_code == 429:
            result_var.set("Error: API request limit reached.")
            result_display.config(fg="red")
            return

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        icon_code = data["weather"][0]["icon"]

        icon_url = "https://openweathermap.org/img/wn/" + icon_code + "@2x.png"

        icon_response = requests.get(icon_url, timeout=10)
        icon_response.raise_for_status()

        icon_image = Image.open(BytesIO(icon_response.content))

        icon_image = ImageTk.PhotoImage(icon_image)

        icon_display.config(image=icon_image)
        icon_display.image = icon_image

        forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

        forecast_params = {
            "q": location,
            "appid": api_key,
            "units": unit
        }

        try:
            forecast_response = requests.get(
                forecast_url,
                params = forecast_params,
                timeout=10
            )

            forecast_response.raise_for_status()

            forecast_data = forecast_response.json()

        except requests.exceptions.RequestException:
            forecast_var.set("Error: Could not load hourly forecast.")
            return

        forecast_text = "Next 6 Hours:\n\n"

        for forecast in forecast_data["list"][:2]:
            forecast_time = forecast["dt_txt"]
            forecast_temperature = forecast["main"]["temp"]
            forecast_condition = forecast["weather"][0]["description"]

            forecast_text += (
                "Time: " + forecast_time +
                "\nTemperature: " + str(round(forecast_temperature, 2)) +
                (" °C" if unit == "metric" else " °F") +
                "\nCondition: " + forecast_condition.title() +
                "\n\n"
            )

        forecast_var.set(forecast_text)

        daily_forecast = {}

        for forecast in forecast_data["list"]:
            date = forecast["dt_txt"].split(" ")[0]

            if date not in daily_forecast:
                daily_forecast[date] = forecast

        daily_text = "Next 5 Days:\n\n"

        for date, forecast in list(daily_forecast.items())[:5]:
            temperature = forecast["main"]["temp"]
            condition = forecast["weather"][0]["description"]

            daily_text += (
                "Date: " + date + 
                "\nTemperature: " + str(round(temperature, 2)) +
                (" °C" if unit == "metric" else " °F") +
                "\nCondition: " + condition.title() + 
                "\n\n"
            )

        daily_forecast_var.set(daily_text)

        
        temperature_unit = "°C" if unit == "metric" else "°F"

        result_var.set(
            "Location: " + location +
            "\nTemperature: " + str(round(temperature,2)) + " " + temperature_unit +
            "\nHumidity: " + str(humidity) + "%" +
            "\nCondition: " + condition.title() + 
            "\nWind Speed: " + str(wind_speed) + " " +
            ("m/s" if unit == "metric" else "mph")
        )

        result_display.config(fg="black")

    except requests.exceptions.Timeout:
        result_var.set("Error: The weather request timed out.")
        result_display.config(fg="red")

    except requests.exceptions.RequestException:
        result_var.set("Error: Could not connect to the weather service.")
        result_display.config(fg="red")

def toggle_unit():
    global unit

    if unit == "metric":
        unit = "imperial"
        unit_button.config(text="Switch to Celsius")
    else:
        unit = "metric"
        unit_button.config(text="Switch to Fahrenheit")

get_weather_button = tk.Button(
    root,
    text="Get Weather",
    command=get_weather
)

get_weather_button.pack(pady=20)

unit_button = tk.Button(
    root,
    text = "Switch to Fahrenheit",
    command = toggle_unit
)

unit_button.pack(pady=10)

def detect_location():
    try:
        response = requests.get(
            "https://ipinfo.io/json",
            timeout = 10
        )

        response.raise_for_status()

        data = response.json()

        city = data.get("city")

        if not city:
            result_var.set("Error: Could not detect your city.")
            result_display.config(fg="red")
            return

        location_entry.delete(0,tk.END)
        location_entry.insert(0,city)

        result_var.set("Location detected: " + city)
        result_display.config(fg="green")

    except requests.exceptions.RequestException:
        result_var.set("Error: Could not detect your location.")
        result_display.config(fg="red")

location_button = tk.Button(
    root,
    text = "Detect my location",
    command = detect_location
)

location_button.pack(pady=10)

root.mainloop()
