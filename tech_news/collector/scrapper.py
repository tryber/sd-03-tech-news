from parsel import Selector
import requests
import time
import re


def fetch_content(url, timeout=3, delay=0.5):
    try:
        # recurso demora muito a responder
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)
    except requests.ReadTimeout:
        # vamos fazer uma nova requisição
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)
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


def no_white_spaces_around(str):
    result = str
    last_character = len(str)
    if result[0] == " ":
        result = result[1: last_character]
        last_character = len(result)
    if result[last_character - 1] == " ":
        result = result[0: last_character - 1]
    return result


def no_list_item_white_spaces(list):
    result = []
    for items in list:
        result.append(no_white_spaces_around(items))
    return result


# Ref.: https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def scrape(fetcher, pages=1):
    source = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
    response = fetcher(source)
    selector = Selector(text=response)
    url = "Link da url"
    title = selector.css(".tec--article__header__title::text").get()
    time = selector.css(".tec--timestamp__item time::attr(datetime)").get()
    writer_text = selector.css(".tec--author__info__link::text").get()
    writer = no_white_spaces_around(writer_text)
    shares_text = selector.css(".tec--toolbar__item::text").get()
    shares_count = int(get_only_numbers(shares_text))
    comments = int(selector.css("#js-comments-btn::attr(data-count)").get())
    summary_html = selector.css(".tec--article__body p").get()
    summary = cleanhtml(summary_html)
    source_list = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = no_list_item_white_spaces(source_list)
    category_list = selector.css("#js-categories a::text").getall()
    categories = no_list_item_white_spaces(category_list)
    return [{
        "url": url,
        "title": title,
        "timestamp": time,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }]
