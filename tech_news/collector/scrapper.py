from parsel import Selector
import requests
from time import sleep

URL_BASE = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def get_urls(sel):
    return sel.css(
        ".tec--list__item .tec--card__title__link::attr(href)").getall()


def get_pages_details(fetcher, url):
    info = {}
    response = fetcher(url=url)
    sel = Selector(response)

    titles = sel.css(".tec--article__header__title::text").get()
    times = sel.css(".tec--timestamp__item time::attr(datetime)").get()
    writer = sel.css(".tec--author__info__link::text").get()
    shares_count = sel.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = sel.css("#js-comments-btn::text").re_first(r"\d+")
    summary = sel.css("div.tec--article__body > p::text").get()
    sources = sel.css(".z--mb-16 a.tec--badge::text").getall()
    categories = sel.css("#js-categories a::text").getall()

    info["url"] = url
    info["title"] = titles
    info["timestamp"] = times
    info["writer"] = writer
    info["shares_count"] = int(shares_count or "0")
    info["comments_count"] = int(comments_count or "0")
    info["summary"] = summary
    info["sources"] = sources
    info["categories"] = categories
    return info


def scrape(fetcher, pages=1):
    end_point = URL_BASE
    news_list = []
    index = 1

    while index <= pages:
        res = fetcher(end_point)
        sel = Selector(res)
        url_list = get_urls(sel=sel)

        for link in url_list:
            data = get_pages_details(fetcher=fetcher, url=link)
            news_list.append(data)

        end_point = sel.css(".tec--btn::attr(href)").get()
        index += 1

    return news_list
