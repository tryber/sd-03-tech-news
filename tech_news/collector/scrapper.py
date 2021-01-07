import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.ReadTimeout:
        sleep(delay)
        return ""
    except requests.HTTPError:
        sleep(delay)
        return ""
    else:
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    page = 1
    all_news = []
    while page <= pages:
        response = fetcher("https://www.tecmundo.com.br/novidades?page={page}")
        selector = Selector(text=response)
        for news in selector.css(
                ".tec--list__item .tec--card__info a::attr(href)").getall():
            news_selector = Selector(text=fetcher(news))
            # clean_data = counts_cleaner(
            #     news_selector.css(".tec--toolbar__item ::text").getall())
            all_news.append({
                "url": news,
                "title": news_selector
                    .css(".tec--article__header__title::text").get(),
                "timestamp": news_selector
                    .css(".tec--timestamp__item time::attr(datetime)").get(),
                "writer": news_selector
                    .css(".tec--author__info__link::text").get(),
                "shares_count": 0,
                "comments_count": 0,
                "summary": news_selector.css(
                    ".tec--article__body *::text").get(),
                "sources": news_selector.css(
                    ".z--mb-16 .tec--badge::text").getall(),
                "categories": news_selector.css(
                    "#js-categories .tec--badge::text").getall()
            })
        page += 1
    return all_news
