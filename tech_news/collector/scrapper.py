import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        sleep(delay)
        response = requests.get(url, timeout=timeout)
    except (requests.exceptions.HTTPError, requests.exceptions.ReadTimeout):
        return ""
    else:
        return response.text    


def format_content(url, selector):
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d")
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(".tec--article__body *::text").get()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories .tec--badge::text").getall()
    if shares_count is None:
        shares_count = "0"
    if comments_count is None:
        comments_count = "0"
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def scrape(fetcher=fetch_content, pages=1):
    scraplist = []
    for page in range(1, pages + 1):
        response_news = fetcher(
            f"https://www.tecmundo.com.br/novidades?page={page}"
        )
        selector_news = Selector(text=response_news)
        for new in selector_news.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall():
            response_new = fetcher(new)
            selector_new = Selector(text=response_new)
            new_obj = format_content(new, selector_new)
            scraplist.append(new_obj)
    return scraplist