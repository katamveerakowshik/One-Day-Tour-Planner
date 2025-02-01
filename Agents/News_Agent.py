from passwrds import news_api
import requests

def news_forecast(city,from_date = None, to_date=None):
    response = requests.get(f'https://newsapi.org/v2/everything?q=(protests OR traffic) AND {city}&from=2025-01-30&to=2025-01-31&sortBy=relevancy &apiKey={news_api}')
    description = []
    for article in response.json()["articles"]:
        description.append(article["description"])
    return description

print(news_forecast('Delhi'))
