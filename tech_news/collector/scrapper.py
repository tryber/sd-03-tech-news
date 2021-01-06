# import ratelimit

# from ratelimit import limits

import time
import requests
# import parsel

from parsel import Selector


def extract_quantity(arg):
    if(len(arg) > 0):
        if(isinstance(arg, list)):
            return int(arg[0])
        else:
            return int(arg)
    else:
        return False


def fetch_content(url, timeout=3, delay=0.5):
    response = requests.get(url, timeout=timeout)
    status_code = response.status_code
    print(f'status code {status_code}')
    if(status_code != 200):
        return ''
    selector = Selector(text=response.text)
    time.sleep(delay)
    return selector


def scrape(fetcher, pages=1):
    news_items = fetcher("https://www.tecmundo.com.br/novidades")
    news_list = []

    for news in news_items.css(".tec--list__item"):
        url = news.css(".tec--card__thumb a::attr(href)").get()
        inner_selector = Selector(requests.get(url).text)
        news_list.append({
            "url":
                url,
            "title":
                news.css(".tec--card__title *::text")
                .get(),
            "timestamp":
                news.css(".tec--timestamp__item.z--font-semibold *::text")
                .get()
                .replace('/', '-'),
            "writer":
                inner_selector.css('.tec--author__info__link *::text')
                .get(),
            "shares_count":
                extract_quantity(
                    inner_selector
                    .css('.z--container .tec--toolbar__item *::text')
                    .re('\\d')),
            "comments_count":
                extract_quantity(
                    inner_selector.css('#js-comments-btn *::text')
                    .re('\\d')
                ),
            "summary":
                ''.join(
                    inner_selector
                    .css('.tec--article__body p:first-child *::text')
                    .getall()
                ),
            "sources":
                inner_selector.css('[class="tec--badge"]::text')
                .getall(),
            "categories":
                inner_selector
                .css('[class="tec--badge tec--badge--primary"]::text')
                .getall()
        })

    print(news_list)


scrape(fetch_content)
