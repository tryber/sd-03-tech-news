import requests


def fetch_content(url, timeout=3, delay=0.5):

    # Requisição do tipo GET
    response = requests.get(url)
    if response.status_code != 200:
        return ""
    else:
        return response.text
    # print(response.headers["Content-Type"])  # conteúdo no formato html


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
