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
    selection = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair."
    )
    if selection == '1':
        input("Digite o título:")
    if selection == '2':
        input("Digite a data no formato aaaa-mm-dd:")
    if selection == '3':
        input("Digite a fonte:")
    if selection == '4':
        input("Digite a categoria:")
    if selection == '5':
        input("Digite o título:")
    if selection == '6':
        input("Digite o título:")
    if selection == '7':
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)
