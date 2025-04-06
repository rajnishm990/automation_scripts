import requests
import json 
from plyer import notification 

country_code = input("Enter the country code for the news: ")
api_key = input("Enter the api key: ")
news = requests.get(
    f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}')
data = json.loads(news.content) 

for i in range(10):
    notification.notify(
        Title=data['articles'][i]['title'][:20],
        message=data['articles'][i]['description'][:44],
        timeout=5,
        toast=False
    )
