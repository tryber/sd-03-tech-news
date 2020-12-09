from time import sleep
from parsel import Selector
import requests


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    sleep(delay)
    try:
        res = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        res = ""
    finally:
        if res == "" or res.status_code != 200:
            return res
        else:
            return res.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    url = f"https://www.tecmundo.com.br/novidades?page={pages}"
    response = fetch_content(url)
    selector = Selector(text=response)
    news = selector.css(".tec--card__title__link::attr(href)").getall()
    return news


if __name__ == "__main__":
    # print(fetch_content('https://www.tecmundo.com.br/novidades'))
    print(fetch_content('https://httpbin.org/delay/1'))
    print(fetch_content('https://httpbin.org/delay/10'))
    print(scrape(fetch_content, 1))
