import requests
import time


BASE_URL = "https://www.tecmundo.com.br/"


def fetch_content(url, timeout=3, delay=0.5):
    time.sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
    except (response.HTTPError, response.ReadTimeout):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    return ""

