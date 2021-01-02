from time import sleep
import requests
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def turn_into_int(selector):
    return 0 if selector is None else int(selector)


def scrape(fetcher, pages=1):
    pages_quantity = int(pages)
    data_list = []
    for i in range(pages_quantity):
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
                    "shares_count": turn_into_int(selector.css(
                        ".tec--toolbar__item::text"
                    ).re_first("\\d+")),
                    "comments_count": turn_into_int(selector.css(
                        "button::attr(data-count)"
                    ).get()),
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

