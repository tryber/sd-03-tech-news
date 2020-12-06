import requests
import time
import parsel

BASE_URL = 'https://www.tecmundo.com.br/novidades'

headers = {'Content-Type': 'text/html; charset=utf-8'}


def sleep(s):
    return time.sleep(s)


def fetch_content(url, timeout=3):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout, headers=headers)
    except requests.exceptions.Timeout:
        return ''
    sleep(0.5)
    return response.text


css_selectors = {
    'title': '.tec--article__header__title::text',
    'timestamp': '#js-article-date ::attr(datetime)',
    'writer': '.tec--author__info__link *::text',
    'shares_count': '.tec--toolbar__item *::text',
    'comments_count': '#js-comments-btn ::text',
    'summary': '.tec--article__body > p:nth-child(1) *::text',
    'sources': 'div.z--mb-16.z--px-16 > div > a ::text',
    'categories': '#js-categories > .tec--badge--primary ::text',
    'url': '.tec--article__footer a.tec--card__title__link::attr(href)'
}


def get_info_by_key(info, selector):
    if info in ['categories',
                'sources',
                'summary',
                'comments_count',
                ]:
        return selector.css(css_selectors[info]).getall()
    return selector.css(css_selectors[info]).get()


def clear_data(data):
    data['summary'] = ''.join(data['summary'])

    data['shares_count'] = [
        int(i) for i in data['shares_count'].split() if i.isdigit()][0]

    data['comments_count'] = [
        int(i) for i in data['comments_count'][1].split() if i.isdigit()][0]

    data['writer'] = data['writer']

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
        '.tec--list__item .tec--card__title__link::attr(href)').getall()
    while count < pages:
        for article in articles_url:
            selector = get_article_page_selector(article, fetcher)
            infos = {key: get_info_by_key(key, selector)
                     for key in css_selectors}
            clean_data = clear_data(infos)
            articles_data.append(clean_data)
        next_page_url = main_page_selector.css('.tec--btn ::attr(href)').get()
        page = fetcher(next_page_url)
        count += 1

    return articles_data
