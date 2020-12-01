import requests


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    res = requests.get(url)
    print(res.text)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    fetch_content('https://www.tecmundo.com.br/novidades')
