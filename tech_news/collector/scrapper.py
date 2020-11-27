import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        # recurso demora muito a responder
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)
    except requests.ReadTimeout:
        # vamos fazer uma nova requisição
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)
    finally:
        if response.status_code != 200:
            return ""
        else:
            return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
