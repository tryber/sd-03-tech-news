import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout).text
        time.sleep(delay)
    except requests.HTTPError:
        return ""
    else:
        return response


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
