import requests
import time


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    else:
        return "" if response.status_code != 200 else response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
