from parsel import Selector
import requests
import time

BASE_URL = "https://www.tecmundo.com.br/novidades"
PAGE_SFX = "?page=2"

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
    # raw_html = fetcher(BASE_URL)
    # selector = Selector(text=raw_html)
    # # Atributos a serem parseados em cada URL
    # for url in selector.css(".tec--card__title__link::attr(href)").getall():
    #     print(url)
    news_sel = Selector(fetch_content('https://www.tecmundo.com.br/mercado/207426-receita-lanca-site-regularizar-cpf-internet-saiba-usar.htm'))
    news_dump.append({
        # "url" = url
        "title": news_sel.css("h1.tec--article__header__title::text").get(),
        "timestamp": news_sel.css("#js-article-date > strong::text").get(),
        "writer": news_sel.css("a.tec--author__info__link::text").get(),
        "shares_count": news_sel.css("div.tec--toolbar__item::text").get(),
        "comments_count": news_sel.css("#js-comments-btn::text").get(),
        "summary": news_sel.css("div.tec--article__body > p *::text").getall(),
        "sources": news_sel.css("div.z--mb-16 a::text").getall(),
        "categories": news_sel.css("#js-categories a::text").getall()
    })
    print(news_dump)
   # while int(PAGE_SFX[-1]) < pages:
    