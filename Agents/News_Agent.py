from Agents.passwrds import news_api
import requests
import datetime
def news_forecast(city,to_date):
    today = datetime.date
    response = requests.get(f'https://newsapi.org/v2/everything?q=(protests OR traffic) AND {city}&from={today}&to={to_date}&sortBy=relevancy &apiKey={news_api}')
    description = []
    for article in response.json()["articles"]:
        description.append(article["description"])
    return description

# print(news_forecast('delhi','2025-03-25'))
