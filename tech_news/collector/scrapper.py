import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    # tratando múltiplas condições de erro usando uma tupla,
    # conforme https://docs.python.org/pt-br/3/tutorial/errors.html
    except (requests.exceptions.HTTPError, requests.exceptions.ReadTimeout):
        return ""
    else:
        return response.text


def get_info(fetcher, url):
    response = fetcher(url=url)
    selector = Selector(text=response)
    data = {}

    data["url"] = url
    data["title"] = selector.css(".tec--article__header__title::text").get()
    data["timestamp"] = selector.css("time::attr(datetime)").get()
    data["writer"] = (selector.css(".tec--author__info__link::text").get())
    shares_count = (
        selector.css("tec--toolbar__item::text").re_first(r"\d+") or "0"
    )
    data["shares-count"] = int(shares_count)
    comments_count = selector.css("button::attr(data-count)").get() or "0"
    data["comments_count"] = int(comments_count)
    data["summary"] = selector.css(".tec--article__body > p::text").get()
    data["sources"] = selector.css(".z--mb-16 div a::text").getall()
    data["categories"] = selector.css(
        ".tec--badge.tec--badge--primary::text"
    ).getall()

    return data


def scrape(fetcher, pages=1):
    BASE_URL = "https://www.tecmundo.com.br/novidades"
    news = []
    for page in range(1, pages + 1):
        url = f"{BASE_URL}?page={page}"
        response = fetcher(url)
        selector = Selector(text=response)
        news_link_list = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for link in news_link_list:
            new = get_info(fetcher, link)
            news.append(new)

    return news


if __name__ == "__main__":
    print(scrape(fetch_content, pages=2))
