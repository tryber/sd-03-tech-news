import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        sleep(delay)
        # Requisição do tipo GET
        response = requests.get(url, timeout=timeout)
        if response.status_code != 200:
            return ""
        else:
            return response.text
        # print(response.headers["Content-Type"])  # conteúdo no formato html
    except (requests.ReadTimeout, requests.HTTPError) as excep:
        print(excep)
        return ''

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
