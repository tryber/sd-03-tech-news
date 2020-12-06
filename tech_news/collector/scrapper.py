from parsel import Selector
from tech_news.database import create_news
import requests
from time import sleep

BASE_URL = "https://www.tecmundo.com.br/novidades?page="
URL_SELECTOR = '.tec--card__title__link::attr(href)'


def digits(input):
    # input == None ? result = 0 : result = int(input[1:[:parsed.find(' ')]])
    if input is None:
        return 0
    else:
        parsed = input[1:]  # Vem com um espaço antes, ignorando este espaço
        sp_char = parsed.find(' ')
        return int(parsed[:sp_char])


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        response = requests.get(url, timeout=timeout)
    else:
        if response.status_code == 200:
            return(response.text)
        return('')
    sleep(delay)
    # Delay para evitar sobrecarga de chamadas


def extract_content(selector, url):
    title = selector.css('h1.tec--article__header__title::text').get()
    time = selector.css('time#js-article-date::attr(datetime)').get()
    writer = selector.css('a.tec--author__info__link::text').get()
    shares = digits(selector.css('div.tec--toolbar__item::text').get())
    comments = digits(selector.css('#button::attr(data-count)').get())
    summary = selector.css('div.tec--article__body > p::text').get()
    sources = selector.css('div.z--mb-16 a::text').getall()
    categories = selector.css('#js-categories a::text').getall()
    return {
        'url': url,
        'title': title,
        'timestamp': time,
        'writer': writer,
        'shares_count': shares,
        'comments_count': comments,
        'summary': summary,
        'sources': sources,
        'categories': categories,
    }


def scrape(pages=1):
    news_dump = []
    curr_page = 1
    while curr_page <= pages:
        homepage_html = fetch_content(f'{BASE_URL}{curr_page}')
        selector = Selector(text=homepage_html)
        # Atributos a serem parseados em cada URL

        for url in selector.css(URL_SELECTOR).getall():
            print('Estamos na página', curr_page, 'URL', url)
            news_sel = Selector(fetch_content(url))
            news_dump.append(extract_content(news_sel, url))

        curr_page += 1
    create_news(news_dump)
    print(f'Foram importadas {len(news_dump)} notícias')
