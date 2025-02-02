from Agents.passwrds import weather_api
import requests

def weather_forecast(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}')
    description = response.json()['weather'][0]['description']
    temperature = response.json()['main']['temp']
    longitute = response.json()['coord']['lon']
    lattitude = response.json()['coord']['lat']
    return description, temperature, longitute, lattitude

print(weather_forecast("delhi"))