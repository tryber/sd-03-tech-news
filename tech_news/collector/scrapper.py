import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.ReadTimeout:
        sleep(delay)
        return ""
    except requests.HTTPError:
        sleep(delay)
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
