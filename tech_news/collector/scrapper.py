import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    time.sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ReadTimeout):
        return ''
    else:
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
