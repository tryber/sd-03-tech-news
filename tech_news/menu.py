import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def create_news(file):
    return file


def collector_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n "
        + "1 - Importar notícias a partir de um arquivo CSV;\n "
        + "2 - Exportar notícias para CSV;\n "
        + "3 - Raspar notícias online;\n "
        + "4 - Sair.\n "
    )

    if user_input == "1":
        file = input("Digite o nome do arquivo CSV a ser importado: ")
        imported = csv_importer(file)
        return create_news(imported)
    elif user_input == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado: ")
        exported = csv_exporter(file)
        return create_news(exported)
    elif user_input == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas: ")
        scraped = scrape(fetcher=fetch_content, pages=int(pages))
        return create_news(scraped)
    elif user_input == "4":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n "
        + "1 - Buscar notícias por título;\n "
        + "2 - Buscar notícias por data;\n "
        + "3 - Buscar notícias por fonte;\n "
        + "4 - Buscar notícias por categoria;\n "
        + "5 - Listar top 5 notícias;\n "
        + "6 - Listar top 5 categorias;\n "
        + "7 - Sair.\n "
    )

    if user_input == "1":
        title = input("Digite o título: ")
        return search_by_title(title)
    elif user_input == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
        return search_by_date(date)
    elif user_input == "3":
        source = input("Digite a fonte: ")
        return search_by_source(source)
    elif user_input == "4":
        category = input("Digite a categoria: ")
        return search_by_category(category)
    elif user_input == "5":
        return top_5_news()
    elif user_input == "6":
        return top_5_categories()
    elif user_input == "7":
        return print("Encerrando script\n")
    else:
        return print("Opção inválida", file=sys.stderr)


if __name__ == "__main__":
    collector_menu()
