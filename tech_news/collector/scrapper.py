from parsel import Selector
import requests
import time


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    sel = Selector(fetcher)
    # for notice in sel.css(".tec--main"):
    titles = sel.css(".tec--article__header__title::text").get()
    timestamp = sel.css(".tec--timestamp__item time::attr(datetime)").get()
    writer = sel.css(".tec--author__info__link::text").get()
    shares_count = sel.css(".tec--toolbar__item::text").getall()
    # shares_count = [int(word) for word in shares.split() if word.isdigit()]
    print(titles, timestamp, writer, shares_count)
