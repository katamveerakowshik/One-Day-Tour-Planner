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
    string_places = ', '.join([f"{place[0]}" for place in places_in_city])

    print('news_end_points, weather, longitute, lattitude :', news_api_endpoints, weather_desc, temperature, lon, lat)
    print('places :', places_in_city)
    print('news :', news_in_city)
    print(string_places)

    model = "deepseek-r1:1.5b"

    prompt = f'''Create a one-day itinerary for {city} that includes the following places: {string_places}. 
              Consider the weather ({weather_desc} and {temperature}), prioritize outdoor activities in good 
              weather, and include breaks for meals. The itinerary should start at {start_time} AM and end by 
            {end_time}PM'''


    response = ollama.generate(model = model, prompt = prompt)

    return response





