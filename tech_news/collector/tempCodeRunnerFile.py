import requests 
import time
import parsel
import re

BASE_URL = 'https://www.tecmundo.com.br/novidades'

headers = {'Content-Type': 'text/html; charset=utf-8'}


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    response = requests.get(url, timeout=3, headers=headers)
    if response.status_code != 200:
        return ''
    # time.sleep(6)
    return response.text 
    
css_selectors = {
    'title': '.tec--article__header__title::text',
    'timestamp': '#js-article-date > strong::text',
    'writer': '.tec--author__info::text',
    'shared_count': 'div.tec--toolbar__item::text',
    'comments_count': '#js-comments-btn::text',
    'summary': '.tec--article__body.z--px-16.p402_premium > p:nth-child(1) *::text',
    'sources': 'div.z--mb-16.z--px-16 > div > a ::text',
    'categories': '.tec--badge::text',
}

def get_info_by_key(info, selector):
    if info in ['categories', 'sources', 'summary'] :
        return selector.css(css_selectors[info]).getall()
    return selector.css(css_selectors[info]).get()

def clean_data(data):
    data['sumamry'] = ''.join(data['summary'])
    data['shared_count'] = re.findall(r'\d+', data['shared_count'])[0]
    return data

def get_article_page_selector(url):
    article_page = requests.get(url, headers=headers).text
    return parsel.Selector(article_page)

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    page = fetcher(BASE_URL)
    # print(page)
    main_page_selector = parsel.Selector(page)

    url_selector = '.tec--list__item .tec--card__title__link::attr(href)'

    article_url = main_page_selector.css(url_selector).getall()[2]

    selector = get_article_page_selector(article_url)

    infos = { key: get_info_by_key(key, selector) for key in css_selectors }

    print(clean_data(infos))
    
scrape(fetch_content)