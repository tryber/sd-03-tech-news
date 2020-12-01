from time import sleep
import requests


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    finally:
        if response.status_code != 200:
            return ""
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
