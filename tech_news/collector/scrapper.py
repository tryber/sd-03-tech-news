import requests
from time import sleep
from parsel import Selector
import re


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    ENDPOINT = '?page='
    response = fetch_content(fetcher)
    selector = Selector(text=response)
    hrefs = []
    data = []
    for href in selector.css(".tec--list__item"):
        hrefs.append(href.css("a::attr(href)").get())

    for page in range(1, pages + 1):
        for url in hrefs:
            new = Selector(text=fetch_content(url + ENDPOINT + str(page)))
            data.append(
                {
                    "url": url,
                    "title": new.css("title::text").get(),
                    "timestamp": new
                    .css("#js-article-date::attr(datetime)").get(),
                    "whiter": new.css(".tec--author__info__link::text").get(),
                    "shares_count": int(re.sub('[^0-9]', '',  (
                        new
                        .css(".tec--toolbar .tec--toolbar__item::text")
                        .get('0')))),
                    "comments_count": int(
                        new
                        .css("#js-comments-btn::attr(data-count)")
                        .get('0')),
                    "summary": ' '.join(
                        new.css(".tec--article__body *::text").getall()
                    ),
                    "sources": new.css(".z--mb-16 .tec--badge::text").getall(),
                    "categories": new
                    .css("#js-categories .tec--badge::text")
                    .getall(),
                }
            )
    return data
