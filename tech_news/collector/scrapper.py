import requests
import time
from parsel import Selector


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.exceptions.Timeout:
        return ""
    else:
        if response.status_code != 200:
            return ""
        return response.text


def get_info(fetcher, url):
    response = fetcher(url=url)
    selector = Selector(text=response)
    info = {}

    info["url"] = url
    title = selector.css(".tec--article__header__title::text").get()
    info["title"] = title
    time = selector.css(".tec--timestamp__item time::attr(datetime)").get()
    info["timestamp"] = time
    writer = selector.css(".tec--author__info__link::text").get()
    info["writer"] = writer
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    info["shares_count"] = int(shares_count or "0")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    info["comments_count"] = int(comments_count or "0")
    summary = selector.css("div.tec--article__body > p::text").get()
    info["summary"] = summary
    sources = selector.css(".z--mb-16 a.tec--badge::text").getall()
    info["sources"] = sources
    categories = selector.css("#js-categories a::text").getall()
    info["categories"] = categories

    return info


def scrape(fetcher, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades"
    counter = 0
    list = []

    while counter < int(pages):
        response = fetcher(base_url)
        selector = Selector(text=response)
        url_list = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()

        for url in url_list:
            info = get_info(fetcher=fetcher, url=url)
            list.append(info)

        counter += 1

    return list
