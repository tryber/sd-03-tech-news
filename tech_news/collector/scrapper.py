from parsel import Selector
from tech_news.database import create_news
import requests
import time

BASE_URL = "https://www.tecmundo.com.br/novidades?page="

def extract_num(input):
    # input == None ? result = 0 : result = int(input[1:[:parsed.find(' ')]]) é o ternário disso
    if input == None:
        return 0
    else:
        parsed = input[1:] # Vem com um espaço antes, ignorando este espaço
        sp_char = parsed.find(' ')
        return int(parsed[:sp_char])

def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        response = requests.get(url, timeout=timeout)
    finally:
        if response.status_code == 200:
            return(response.text)
        else:
            return('')
    time.sleep(delay)
    # Delay para evitar sobrecarga de chamadas

def scrape(fetcher, pages=1):
    news_dump = []
    current_page = 1
    raw_html = fetcher(BASE_URL)
    selector = Selector(text=raw_html)
    # Atributos a serem parseados em cada URL
    while current_page <= pages:
        for url in selector.css(".tec--card__title__link::attr(href)").getall():
            print('Estamos na página', current_page, 'URL', url)
            news_sel = Selector(fetch_content(url))
            news_dump.append({
                "url": url,
                "title": news_sel.css("h1.tec--article__header__title::text").get(),
                "timestamp": news_sel.css("time#js-article-date::attr(datetime)").get(),
                "writer": news_sel.css("a.tec--author__info__link::text").get(),
                "shares_count": extract_num(news_sel.css("div.tec--toolbar__item::text").get()),
                "comments_count": news_sel.css("#js-comments-btn::attr(button)").get(),
                "summary": ' '.join(news_sel.css("div.tec--article__body > p *::text").getall()),
                "sources": news_sel.css("div.z--mb-16 a::text").getall(),
                "categories": news_sel.css("#js-categories a::text").getall()
            })
        current_page += 1
    print('Resultato finale:', news_dump)
    create_news(news_dump)
