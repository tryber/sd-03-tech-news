import requests
import time
import parsel


URL_BASE = "https://www.tecmundo.com.br/"


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text


def extract_news_page(selector, url):
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    summary = selector.css("div.tec--article__body > p::text").get()
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()

    page = {
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
    return page


def scrape(fetcher, pages=1):
    news_page = []
    selector = parsel.Selector(fetcher(URL_BASE + "novidades/"))
    for _ in range(pages):
        urls = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for url in urls:
            new_selector = parsel.Selector(fetcher(url))
            news_page.append(extract_news_page(new_selector, url))

    return news_page
