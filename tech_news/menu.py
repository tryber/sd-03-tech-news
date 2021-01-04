import sys
from tech_news.database import create_news
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape


def collector_menu():
    option = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Importar notícias a partir de um arquivo CSV;\n "
        "2 - Exportar notícias para CSV;\n "
        "3 - Raspar notícias online;\n "
        "4 - Sair."
    )
    if option == "1":
        file = input("Digite o nome do arquivo CSV a ser importado: ")
        data = csv_importer(file)
        create_news(data)
    elif option == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado: ")
        csv_exporter(file)
    elif option == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas: ")
        data = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(data)
    elif option == "4":
        return print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
