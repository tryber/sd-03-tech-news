import requests
from parsel import Selector
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        if response.status_code != 200:
            return ""
        else:
            return response.text
    except requests.ReadTimeout:
        return ""


def scrape(fetcher, pages=1):
    page_list = []
    for page in range(pages):
        response = fetcher(
            f"https://www.tecmundo.com.br/novidades?page={page}"
        )
        selector = Selector(text=response)
        for news in selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall():
            second_selector = Selector(text=fetcher(news))
            page_list.append({
                "url": news,
                "title": second_selector.css(
                    ".tec--article__header__title::text"
                ).get(),
                "timestamp": second_selector.css(
                    "#js-article-date::attr(datetime)"
                ).get(),
                "writer": second_selector.css(
                    ".tec--author__info__link::text"
                ).get(),
                "shares_count": int(second_selector.css(
                    ".tec--toolbar__item::text"
                ).re_first(r"\d")),
                "comments_count": int(second_selector.css(
                    "#js-comments-btn::attr(data-count)"
                ).get()),
                "summary": second_selector.css(
                    ".tec--article__body p *::text"
                ).get(),
                "sources": second_selector.css(
                    ".z--mb-16 .tec--badge::text"
                ).getall(),
                "categories": second_selector.css(
                    "#js-categories .tec--badge::text"
                ).getall(),
            })
    return page_list
