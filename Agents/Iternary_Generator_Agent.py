import ollama
from Agents.weather_Agent import  weather_forecast
from Agents.Places_Agent import places
from Agents.News_Agent import news_forecast

def generate_itinerary(city, date,start_time, end_time, interests, starting_point):
    hashh = {"Historical Sites": 'man_made',
             'Food': 'catering',
             'Religion': 'religion',
             'Nature': 'nature',
             'Adventure': 'camping',
             'Sports': 'sport',
             'Shopping': 'commercial'}

    news_api_endpoints = []
    for i in interests:
        news_api_endpoints.append(hashh[i])
    weather_desc, temperature, lon, lat = weather_forecast(city)
    places_in_city = places(lon,lat,news_api_endpoints)
    news_in_city = news_forecast(city,date)

    model = "deepseek-r1:1.5b"

    prompt = f"""
    Using the following details, create a detailed one-day trip itinerary:
    - City: {city}
    - Date: {date}
    - Start Time: {start_time}
    - End Time: {end_time}
    - Starting Point: {starting_point}
    - Weather: {weather_desc}, Temperature: {temperature}°F
    it is the weather on the trip day at the trip location
    - Available Attractions: {', '.join([f"{place[0]} (Lon: {place[1]}, Lat: {place[2]})" for place in places_in_city])}
    Use best of these attractions to make itinerary, all these attractions are aroumd the {city} within 5km radius
    - News Alerts: {news_in_city if news_in_city else "No major disruptions reported"}
    If the news provided are harmless for the trip just avoid them

    **Requirements for the Itinerary:**
    1. Optimize the schedule to maximize the number of attractions visited within the available time.
    2. Include realistic time estimates for each activity and travel between locations.
    3. Provide transportation options between attractions (e.g., walking, public transit).
    4. Recommend dining options near the attractions or along the route.
    5. Use weather information to suggest appropriate clothing and gear (e.g., umbrella, jacket).
    6. Avoid areas affected by any reported disruptions in the news.

    **Format the response as follows:**

    ### [{city}]  One-Day Itinerary for [{date}]

    **Weather Advisory:** [Clothing/gear recommendations]

    **Schedule:**
    Time | Activity | Location | Details
    -----|----------|----------|---------
    [Start Time] | [Activity 1] | [Attraction 1 Name] | [Duration + transportation method]
    ... | ... | ... | ...

    **Dining Recommendations:** 
    [List of dining options with approximate times]

    **Key Tips:** 
    - Peak hours to avoid
    - Special considerations based on weather or news
    """

    response = ollama.generate(model = model, prompt = prompt)

    return response





