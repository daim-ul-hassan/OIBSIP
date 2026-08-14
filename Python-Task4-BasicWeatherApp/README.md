# Weather App

A Python weather application built for the OIBSIP Python Programming Internship.

The project includes two versions:

- Beginner CLI weather application
- Advanced Tkinter GUI weather application

Both versions use the OpenWeatherMap API to retrieve real-time weather information.

## Features

### Beginner Version

The Beginner version is a command-line weather application.

Features:

- City name or ZIP code input
- Real-time weather data
- Temperature in Celsius
- Temperature in Fahrenheit
- Humidity percentage
- Weather condition
- Wind speed
- Empty input validation
- City not found handling
- Invalid API key handling
- Network timeout handling
- API connection error handling

### Advanced Version

The Advanced version provides a graphical weather application with additional functionality.

Features:

- Tkinter graphical interface
- City name or ZIP code input
- Get Weather button
- Current weather information
- Weather condition icons
- Pillow image handling
- Next 6 hours forecast
- Next 5 days forecast
- Celsius/Fahrenheit toggle
- Automatic approximate location detection using IP address
- GUI-based error messages
- Invalid API key handling
- City not found handling
- Network timeout handling
- API connection error handling

## Weather Information

The application displays:

- Temperature
- Humidity
- Weather condition
- Wind speed
- Weather icon
- Hourly forecast
- Daily forecast

## Technologies Used

### Beginner

- Python
- Requests
- JSON
- python-dotenv
- OpenWeatherMap API

### Advanced

- Python
- Tkinter
- Requests
- JSON
- python-dotenv
- Pillow
- OpenWeatherMap API
- ipinfo.io API

## Project Structure

```text
Python-Task4-BasicWeatherApp/
│
├── weather.py
├── advanced_weather.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore