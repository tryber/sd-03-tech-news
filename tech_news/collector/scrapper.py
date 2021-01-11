import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except (requests.exceptions.HTTPError, requests.exceptions.ReadTimeout):
        return ""
    else:
        return response.text


def new_scraper(url, fetcher):
    selector = Selector(text=fetcher(url))
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    summary = selector.css("div.tec--article__body > p::text").get()
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count or "0"),
        "comments_count": int(comments_count or "0"),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def scrape(fetcher, pages=1):
    data_list = []
    for i in range(1, pages + 1):
        print(i)
        page = Selector(
            text=fetcher(f"https://www.tecmundo.com.br/novidades?page={i}")
        )
        urls = page.css(
            ".tec--list .tec--card__title__link::attr(href)"
        ).getall()
        print(urls)
        for url in urls:
            data_list.append(new_scraper(url, fetcher))
    return data_list
