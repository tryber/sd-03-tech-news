import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    response = requests.get(url, timeout=3)
    time.sleep(delay)
    if response.status_code != 200:
        return ""
    return response.text


def scrape(fetcher, pages=1):
    for i in range(pages):
        selector = Selector(text=fetcher("https://www.tecmundo.com.br/novidades"))
        all_link = selector.css(".tec--card__title__link::attr(href)").getall()
        for link in all_link:
            selector = Selector(text=fetcher(link))
            url=link
            title=selector.css('.tec--article__header__title')
            timestamp=selector.css('.tec--timestamp__item::attr(datetime)')
            writer=selector.css('.tec--author__info__link::text')
            shares_count=selector.css('')
            comments_count=selector.css('')
            summary=selector.css('')
            sources=selector.css('')
            categories=selector.css('')


