from Agents.passwrds import weather_api
import requests


def weather_forecast(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}')

    data = response.json()

    description = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']

    # Convert temperature from Kelvin to Celsius
    temperature_celsius = round(temperature_kelvin - 273.15, 2)

    wind_speed = data['wind']['speed']

    humidity = data['main']['humidity']

    longitute = data['coord']['lon']

    lattitude = data['coord']['lat']

    return description, temperature_celsius, longitute, lattitude, wind_speed, humidity

# print(weather_forecast("delhi"))