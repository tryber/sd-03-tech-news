import requests
from time import sleep
from parsel import Selector

URL_BASE = "https://www.tecmundo.com.br/"


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def get_detail_content(fetcher, url):
    info = {}
    response = fetcher(url=url)
    get_selector = Selector(response)

    titles = get_selector.css(".tec--article__header__title::text").get()
    times = get_selector.css(
        ".tec--timestamp__item time::attr(datetime)").get()
    writer = get_selector.css(".tec--author__info__link::text").get()
    shares_count = get_selector.css(
        ".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = get_selector.css(
        "#js-comments-btn::text").re_first(r"\d+")
    summary = get_selector.css("div.tec--article__body > p::text").get()
    sources = get_selector.css(".z--mb-16 a.tec--badge::text").getall()
    categories = get_selector.css("#js-categories a::text").getall()

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


def get_url_list(get_selector):

    return get_selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)").getall()


def mount_information(fetcher, urls_list):
    params_list = []
    for detail_url in urls_list:
        info = get_detail_content(fetcher=fetcher, url=detail_url)
        params_list.append(info)
    return params_list


def scrape(fetcher, pages=1):
    last_url = URL_BASE+"novidades"
    data_list = []
    i = 1

    while i <= pages:
        response = fetcher(last_url)
        get_selector = Selector(response)
        list = get_url_list(get_selector=get_selector)
        data = mount_information(fetcher=fetcher, urls_list=list)
        data_list.extend(data)
        last_url = get_selector.css(".tec--btn::attr(href)").get()
        i += 1

    return data_list
