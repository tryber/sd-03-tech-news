# from parsel import Selector
import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError) as excep:
        print(excep)
        return ''
    else:
        return response.text
