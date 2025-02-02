import requests
from Agents.passwrds import places_api

def places(long, lat, interests):
    common = ['service', 'tourism', 'public_transport']
    interests = interests + common
    str_interests = ','.join(f"{interest}" for interest in interests)
    response = requests.get(f"https://api.geoapify.com/v2/places?categories={str_interests}&filter=circle:{long},{lat},5000&limit=100&apiKey={places_api}")
    places = []
    for place in response.json()['features']:
        place_name = place['properties']['name']
        place_lon = place['properties']['lon']
        place_lat = place['properties']['lat']
        places.append([place_name, place_lon, place_lat])
    return places

print(places('77.22445','28.63576', ['sport', 'ski'] ))