import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code != 200:
            return ""
        else:
            return response.text
    except requests.ReadTimeout:
        return ""


def scrape(fetcher, pages=1):
    notices = []
    for p in range(int(pages)):
        selector = Selector(
            text=fetcher("https://www.tecmundo.com.br/novidades")
        )
        allNotices = selector.css(
            ".tec--list .tec--card__title__link::attr(href)"
        ).getall()
        for url in allNotices:
            selector = Selector(text=fetcher(url))
            notices.append({
                "url": url,
                "title": selector.css(
                    ".tec--article__header__title::text"
                ).get(),
                "timestamp": selector.css(
                    "#js-article-date::attr(datetime)"
                ).get(),
                "writer": selector.css(".tec--author__info__link::text").get(),
                "shares_count": int(selector.css(
                    ".tec--toolbar__item::text"
                ).re_first(r"\d+")),
                "comments_count": int(selector.css(
                    "#js-comments-btn::attr(data-count)"
                ).get()),
                "summary": selector.css(".tec--article__body > p::text").get(),
                "sources": selector.css(".z--mb-16 div a::text").getall(),
                "categories": selector.css(
                    ".tec--badge.tec--badge--primary::text"
                ).getall()
            })
    return notices
