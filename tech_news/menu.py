from tech_news.collector.exporter import csv_exporter
from tech_news.collector.importer import csv_importer
from tech_news.collector.scrapper import scrape
from tech_news.collector.scrapper import fetch_content
from tech_news.database import create_news
import sys


def collector_menu():
    selection = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Importar notícias a partir de um arquivo CSV;\n "
        "2 - Exportar notícias para CSV;\n "
        "3 - Raspar notícias online;\n "
        "4 - Sair."
    )
    if selection == "1":
        file = input("Digite o nome do arquivo CSV a ser importado:")
        data = csv_importer(file)
        create_news(data)
    elif selection == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(file)
    elif selection == "3":
        n = input("Digite a quantidade de páginas a serem raspadas:")
        data = scrape(fetcher=fetch_content, pages=int(n))
        create_news(data)
    elif selection == "4":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
