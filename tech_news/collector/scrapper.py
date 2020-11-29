import requests
import time


BASE_URL = "https://www.tecmundo.com.br/"


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    return ""
