import requests

def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        status_code = response.status_code
        if(status_code != 200):
            return ''
        selector = Selector(text=response.text)
        request_result = selector.get()

        sleep(delay)

        return request_result
    except requests.exceptions.Timeout:
        return ''


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
