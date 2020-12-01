import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(delay)
    except requests.readTimeout:
        response = []
    finally:
        if response.status_code != 200:
            return ""
    return response.text


def scrape(fetcher, pages=1):
    data_list = []
    for i in range(pages):
        selector = Selector(
            text=fetcher("https://www.tecmundo.com.br/novidades/")
        )
        all_link = selector.css(
            ".tec--list .tec--card__title__link::attr(href)"
        ).getall()
        for link in all_link:
            selector = Selector(text=fetcher(link))
            data_list.append(
                {
                    "url": link,
                    "title": selector.css(
                        ".tec--article__header__title::text"
                    ).get(),
                    "timestamp": selector.css("time::attr(datetime)").get(),
                    "writer": selector.css(
                        ".tec--author__info__link::text"
                    ).get(),
                    "shares_count": selector.css(
                        ".tec--toolbar__item::text"
                    ).re_first("\\d+") or 0,
                    "comments_count": selector.css(
                        "button::attr(data-count)"
                    ).get() or 0,
                    "summary": selector.css(
                        ".tec--article__body > p::text"
                    ).get(),
                    "sources": selector.css(".z--mb-16 div a::text").getall(),
                    "categories": selector.css(
                        ".tec--badge.tec--badge--primary::text"
                    ).getall(),
                }
            )
    return data_list


print(scrape(fetch_content, 2))
