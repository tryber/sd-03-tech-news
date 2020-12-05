from parsel import Selector
import requests
from time import sleep
import re


def fetch_content(url, timeout=3, delay=0.5):
    try:
        # recurso demora muito a responder
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        # vamos fazer uma nova requisição
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.HTTPError:
        return ""
    finally:
        if response.status_code != 200:
            return ""
        else:
            return response.text


def get_only_numbers(str):
    result = ""
    for character in str:
        if re.search("[0-9]", character):
            result = result + character
    return result


def no_list_item_white_spaces(list):
    result = []
    for items in list:
        result.append(items.strip())
    return result


# Ref.: https://bit.ly/2JPEQ8z
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def get_resume(fetcher, url):
    source = url
    response = fetcher(source)
    selector = Selector(text=response)
    url = f"{source}"
    title = selector.css(".tec--article__header__title::text").get()
    time = selector.css(".tec--timestamp__item time::attr(datetime)").get()
    writer_text = selector.css("div.tec--timestamp__item a::text").get()
    if not writer_text:
        writer_text = selector.css(".tec--author__info__link::text").get()
    if not writer_text:
        writer = "Unknown"
    else:
        writer = writer_text.strip()
    shares_text = selector.css(".tec--toolbar__item::text").get()
    shares_count = 0
    if shares_text:
        shares_count = int(get_only_numbers(shares_text))
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    summary_html = selector.css(".tec--article__body p").get()
    if summary_html:
        summary = cleanhtml(summary_html)
    else:
        summary = "Do not get summary"
    source_list = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = no_list_item_white_spaces(source_list)
    category_list = selector.css("#js-categories a::text").getall()
    categories = no_list_item_white_spaces(category_list)
    return {
        "url": url,
        "title": title,
        "timestamp": time,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }


def scrape(fetcher, pages=1):
    news_summary = []
    next_page = "https://www.tecmundo.com.br/novidades/"
    n = 0
    while n < pages:
        response = fetcher(next_page)
        selector = Selector(text=response)
        for url in selector.css("div.tec--list__item"):
            link = url.css("a.tec--card__title__link::attr(href)").get()
            news_summary.append(get_resume(fetcher, link))
        next_page = selector.css(".tec--btn::attr(href)").get()
        n += 1

    return news_summary
