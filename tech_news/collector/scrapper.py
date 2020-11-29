import requests
""" import time """
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
    'writer': '.tec--timestamp__item *::text',
    'shared_count': 'div.tec--toolbar__item *::text',
    'comments_count': '#js-comments-btn *::text',
    'summary': '.tec--article__body > p:nth-child(1) *::text',
    'sources': 'div.z--mb-16.z--px-16 > div > a ::text',
    'categories': '.tec--badge::text',
    'next_btn': '.tec--btn ::attr(href)',
    'article_url': '.tec--list__item .tec--card__title__link::attr(href)'
}


def get_info_by_key(info, selector):
    if info in ['categories', 'sources', 'summary', 'writer', 'comments_count', 'shared_count']:
        return selector.css(css_selectors[info]).getall()
    return selector.css(css_selectors[info]).get()


def clear_data(data):
    data['summary'] = ''.join(data['summary'])
    data['shared_count'] = re.findall("\d+", data['shared_count'][0])

    data['writer'] = data['writer'][0]
    return data


def get_article_page_selector(url, fetcher):
    article_page = fetcher(url)
    return parsel.Selector(article_page)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    page = fetcher(BASE_URL)
    # print(page)
    count = 0
    articles_data = []
    main_page_selector = parsel.Selector(page)
    articles_url = main_page_selector.css(
        css_selectors['article_url']).getall()
    while count < pages:
        for article in articles_url:
            selector = get_article_page_selector(article, fetcher)
            infos = {key: get_info_by_key(key, selector)
                     for key in css_selectors}
            clean_data = clear_data(infos)
            articles_data.append(clean_data)
        next_page_url = main_page_selector.css(css_selectors['next_btn']).get()
        page = fetcher(next_page_url)
        count += 1

    return print(len(articles_data))


scrape(fetch_content, 2)
