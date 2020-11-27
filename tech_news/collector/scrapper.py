import requests
import time


def fetch_content(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(0.5)
    except requests.HTTPError:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
