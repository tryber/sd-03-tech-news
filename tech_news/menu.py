import sys
from collector.importer import csv_importer
from collector.exporter import csv_exporter
from collector.scrapper import scrape, fetch_content
from analyzer.ratings import top_5_categories, top_5_news
from analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)


def collector_menu():
    options = """Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair."""

    request_options = {
        "1": "Digite o nome do arquivo CSV a ser importado:",
        "2": "Digite o nome do arquivo CSV a ser exportado",
        "3": "Digite a quantidade de páginas a serem raspadas:",
    }

    call_options = {
        "1": lambda path: csv_importer(path),
        "2": lambda path: csv_exporter(path),
        "3": lambda pages: scrape(fetcher=fetch_content, pages=int(pages)),
    }

    try:
        create_news()
        option = input(options)
        if option in request_options.keys():
            path = input(request_options[option])
            result = call_options[option](path)
            print(result)
        else:
            print("Opção inválida", file=sys.stderr)
    except (KeyError, TypeError):
        raise ValueError("Opção inválida\n")
    finally:
        print("Encerrando script\n")


def create_news():
    with open("correct.csv"):
        pass
    pass


def analyzer_menu():
    options = """Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""

    request_options = {
        "1": lambda: print("Digite o título:"),
        "2": lambda: print("Digite a data no formato aaaa-mm-dd:"),
        "3": lambda: print("Digite a fonte:"),
        "4": lambda: print("Digite a categoria:"),
        "5": lambda: print(top_5_news()),
        "6": lambda: print(top_5_categories()),
    }

    call_options = {
        "1": lambda search: search_by_title(search),
        "2": lambda search: search_by_date(search),
        "3": lambda search: search_by_source(search),
        "4": lambda search: search_by_category(search),
    }

    try:
        option = input(options)
        if option in request_options.keys():
            request_options[option]()
        else:
            print("Opção inválida", file=sys.stderr)
        if option in call_options.keys():
            path = input()
            result = call_options[option](path)
            print(result)

    except (KeyError, TypeError, IndexError):
        raise ValueError("Opção inválida\n")
    finally:
        print("Encerrando script\n")
