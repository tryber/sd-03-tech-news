import requests
from time import sleep
from parsel import Selector

BASE_URL = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text

    except (requests.ReadTimeout, requests.HTTPError):
        return ""


def get_information(url):
    info = {}
    data = fetch_content(url)
    selector = Selector(text=data)
    info['url'] = url
    info['title'] = selector.css('.tec--article__header__title::text').get()
    info['timestamp'] = (selector.css('.tec--timestamp__item strong::text')
                         .get())
    info['writer'] = selector.css('.tec--author__info__link::text').get()
    shares = (selector.css('.tec--toolbar__item::text')
              .re_first(r'\d*') or "0")
    info['shares_count'] = int(shares)
    info['comments_count'] = (selector.css('#js-comments-btn::attr(data-count)')
                              .get())
    summaryArray = (selector.css('.tec--article__body  p:nth-child(1) *::text')
                    .getall())
    info['summary'] = ''.join(summaryArray)
    info['sources'] = selector.css('.tec--badge::text').get()
    info['categories'] = selector.css('.tec--badge--primary::text').getall()

    return info


def scrape(fetcher, pages=1):
    content = fetcher(url=BASE_URL)
    selector = Selector(text=content)
    links = selector.css('.tec--card__title__link::attr(href)').getall()

    infos = map(get_information, links)
    return list(infos)
