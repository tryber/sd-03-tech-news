import ratelimit

from ratelimit import limits

import time
import requests
import parsel

from parsel import Selector

def fetch_content(url, timeout=3, delay=0.5):
    response = requests.get(url, timeout=timeout)
    status_code = response.status_code
    print(status_code)
    if(status_code != 200):
        return ''
    selector = Selector(text=response.text)
    time.sleep(delay)
    return selector


def scrape(fetcher, pages=1):
    news_items = fetcher("https://www.tecmundo.com.br/novidades").css(".tec--list__item")
    news_list = []
    
    def extract_quantity(arg):
        if(isinstance(arg, list) and len(arg) > 0):
            return int(arg[0])
        else:
            return int(arg)

    for news in news_items:
        url = news.css(".tec--card__thumb a::attr(href)").get()
        inner_selector = Selector(requests.get(url).text)
        news_list.append({
            "url": url,
            "title": news.css(".tec--card__title *::text").get(),
            "timestamp": news.css(".tec--timestamp__item.z--font-semibold *::text").get().replace('/', '-'),
            "writer": inner_selector.css('.tec--author__info__link *::text').get(),
            "shares_count": extract_quantity(inner_selector.css('.z--container .tec--toolbar__item *::text').re('\d')),
            "comments_count": extract_quantity(inner_selector.css('#js-comments-btn *::text').re('\d')),
            "summary": inner_selector.css('.tec--article__body p em,a:first-child::text').getall()[0]
        })
    return news_list

print(scrape(fetch_content))