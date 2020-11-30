import requests
import time
from parsel import Selector


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    else:
        if response.status_code != 200:
            return ""
        else:
            return response.text


def appendArr(infos, link, arr):
    title = infos.css(".tec--article__header__title::text").get()
    timestamp = infos.css(".tec--timestamp__item time::attr(datetime)").get()
    writer = infos.css(".tec--author__info__link::text").get()
    shares_count = infos.css(".tec--toolbar__item::text").get()
    try:
        suffix = " Compartilharam"
        if shares_count.endswith(suffix):
            shares_count = shares_count[: -len(suffix)]
    except AttributeError:
        shares_count = 0
    comments_count = infos.css(".tec--btn::attr(data-count)").get()
    summary = infos.css(".tec--article__body *::text").get()
    sources = infos.css(".z--mb-16 .tec--badge::text").getall()
    categories = infos.css(".tec--badge--primary::text").getall()
    arr.append(
        {
            "url": link,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "shares_count": int(shares_count),
            "comments_count": int(comments_count),
            "summary": summary,
            "sources": sources,
            "categories": categories,
        }
    )


def scrape(fetcher=fetch_content, pages=1):
    arr = []
    for i in range(pages):
        page = fetcher(f"https://www.tecmundo.com.br/novidades?page={i}")
        selector = Selector(text=page)
        links = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for link in links:
            second_response = fetcher(link)
            infos = Selector(text=second_response)
            appendArr(infos, link, arr)
    print(len(arr))
    return arr
