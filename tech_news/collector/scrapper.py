import requests
import parsel
import time


BASE_URL = "https://www.tecmundo.com.br/"
BASE_URL1 = "https://www.tecmundo.com.br/mercado/207438-google-abre-processo-estagio-brasil-veja-candidatar.htm"


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def page_new_scrape(selector, url):
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time#js-article-date *::text").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = selector.css("div.tec--toolbar__item::text").get()
    comments_count = selector.css("button#js-comments-btn::text").get()
    summary = selector.css("div.tec--article__body > p::text").get()
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def scrape(fetcher, pages=1):
    news = []
    selector = parsel.Selector(fetcher(BASE_URL1))
    for _ in range(pages):
        urls = selector.css(".tec--list__item")
        print("len de urls", len(urls), *urls, sep="\n")
        for url in urls:
            new_selector = parsel.Selector(fetcher(url))
            news.append(page_new_scrape(new_selector, url))

    return news
