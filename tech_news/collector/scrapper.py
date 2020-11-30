import requests
import time

def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except:
        return ""

    if response.status_code == 200:
        return response.text
    else:
        return ""
    time.sleep(delay)

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
