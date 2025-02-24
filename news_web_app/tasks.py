from celery import shared_task
import requests
from django.conf import settings
import logging

logger = logging.getLogger('news-logger')
headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }

logger = logging.getLogger("news-logger")

@shared_task
def add(x, y):
    return x + y

@shared_task
def print_hello():
    logger.info("Hello World !")
    print("Hello, World!")


@shared_task
def get_latest_news(country=None, language=None, domain=None):
    api_key = settings.NEWS_API_KEY
    param_key = ""
    if country:
        param_key += f"&country={country}"
    if language:
        param_key += f"&language={language}"
    if domain:
        param_key += f"&domain={domain}"
    url = f'https://newsdata.io/api/1/latest?apikey={api_key}{param_key}'
    new_res = requests.get(url, headers=headers)
    data = new_res.json()
    if data["status"] == "success":
        logger.info("News fetched successfully")
        final_data = data["results"]
    else:
        logger.debug("Error while fetching news")
        final_data = []
    return final_data