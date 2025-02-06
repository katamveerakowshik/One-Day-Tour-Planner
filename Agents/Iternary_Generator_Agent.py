import ollama
from Agents.weather_Agent import weather_forecast
from Agents.Places_Agent import places
from Agents.News_Agent import news_forecast
from geopy.distance import geodesic


def generate_itinerary(city, date, start_time, end_time, interests, starting_point):
    hashh = {
        "Historical Sites": 'man_made',
        'Food': 'catering',
        'Religion': 'religion',
        'Nature': 'nature',
        'Adventure': 'camping',
        'Sports': 'sport',
        'Shopping': 'commercial'
    }

    # Map interests to categories and fetch data from APIs
    news_api_endpoints = [hashh[i] for i in interests]
    weather_desc, temperature, lon, lat, wind_speed, humidity = weather_forecast(city)
    places_in_city = places(lon, lat, news_api_endpoints)
    news_in_city = news_forecast(city, date)

    # Sort places by proximity to the starting point (if coordinates available)
    def calculate_distance(loc1, loc2):
        return geodesic(loc1, loc2).km

    starting_coords = (lat, lon)
    places_in_city.sort(key=lambda x: calculate_distance(starting_coords, (x[2], x[1])))

    string_places = ', '.join([f"{place[0]}" for place in places_in_city])

    model = "deepseek-r1:7b"

    prompt = f"""
    Create a one-day itinerary for a user in the city of {city} on {date}. The user’s preferences and constraints are as follows:

    1. Time Details:
       - Start time: {start_time}
       - End time: {end_time}
       - Starting position: {starting_point}

    2. Places to Visit:
       Based on the user’s interests and preferences, here is a list of recommended places in the city:
       {string_places}

    3. Weather Details:
       The current weather in the city is as follows:
       - Temperature: {temperature}°C
       - Weather conditions: {weather_desc}
       - Wind speed: {wind_speed} km/h
       - Humidity: {humidity}%

    4. News and Alerts:
       Consider the following news updates or interruptions that may affect the itinerary:
       {news_in_city}

    Requirements for the Itinerary:
    - Suggest an efficient route starting from the given starting position.
    - Prioritize places based on proximity, user interests, and weather conditions.
    - Allocate time slots for each place, ensuring enough time for travel and exploration.
    - Include meal or break recommendations at appropriate times.
    - Avoid areas affected by disruptions mentioned in the news updates.

    Provide a detailed itinerary with time slots and brief descriptions of each activity or location.
    """

    response = ollama.generate(model=model, prompt=prompt)

    return response.json(), places_in_city, lat, lon




