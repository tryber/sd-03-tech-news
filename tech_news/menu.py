import sys
from tech_news.database import create_news
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


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
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair."
    )
    if option == "1":
        title = input("Digite o título: ")
        search = search_by_title(title)
        print(search)
    elif option == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
        search = search_by_date(date)
        print(search)
    elif option == "3":
        source = input("Digite a fonte: ")
        search = search_by_source(source)
        print(search)
    elif option == "4":
        category = input("Digite a categoria: ")
        search = search_by_category(category)
        print(search)
    elif option == "5":
        news = top_5_news()
        print(news)
    elif option == "6":
        news = top_5_categories()
        print(news)
    elif option == "7":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)
