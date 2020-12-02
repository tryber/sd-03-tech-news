import requests
from time import sleep
import parsel


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def crawling_page(url, fetcher):
    selector = parsel.Selector(fetcher(url))
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
    news = []
    url = "https://www.tecmundo.com.br/novidades/"

    for _ in range(pages):
        print("here", _, url)
        if not url:
            break
        selector = parsel.Selector(fetcher(url))
        news_urls = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        news.extend(
            [crawling_page(news_url, fetcher) for news_url in news_urls]
        )
        url = selector.css(".tec--btn::attr(href)").get()
    return news
