import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    strvar = ""
    # Faz uma request com um timeout de até 3 segundos e só refaz após o delay
    response = requests.get(url, timeout=timeout)
    # Analisa se houve uma resposta do server.
    if response.status_code != 200:
        return strvar
    else:
        return response.text
    time.sleep(delay)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
