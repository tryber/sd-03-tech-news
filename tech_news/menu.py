import sys

# from tech_news.collector import exporter, importer, scrapper
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)

options = """Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair."""

next_step = {
    "1": "Digite o nome do arquivo CSV a ser importado:",
    "2": "Digite o nome do arquivo CSV a ser exportado",
    "3": "Digite a quantidade de páginas a serem raspadas:",
}

module_to_use = {
    "1": lambda path: csv_importer(path),
    "2": lambda path: csv_exporter(path),
    "3": lambda pages: scrape(fetcher=fetch_content, pages=int(pages)),
}


def collector_menu():
    try:
        create_news()
        print(options)
        choice = input()
        if choice in next_step.keys():
            print(next_step[choice])
            path = input()
            result = module_to_use[choice](path)
            print(result)
        else:
            print("Opção inválida", file=sys.stderr)
    except (KeyError, TypeError):
        raise ValueError("Opção inválida\n")
    finally:
        print("Encerrando script\n")


# collector_menu()


def analyzer_menu():
    options = """Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""

    next_step = {
        "0": lambda: print(),
        "1": lambda: print("Digite o título:"),
        "2": lambda: print("Digite a data no formato aaaa-mm-dd:"),
        "3": lambda: print("Digite a fonte:"),
        "4": lambda: print("Digite a categoria:"),
        "5": lambda: print(top_5_news()),
        "6": lambda: print(top_5_categories()),
    }

    module_to_use = {
        "0": lambda test: print(options),
        "1": lambda search: search_by_title(search),
        "2": lambda search: search_by_date(search),
        "3": lambda search: search_by_source(search),
        "4": lambda search: search_by_category(search),
    }

    try:
        print(options)
        choice = input()
        if choice in next_step.keys():
            next_step[choice]()
        else:
            print("Opção inválida", file=sys.stderr)
        if choice in module_to_use.keys():
            path = input()
            result = module_to_use[choice](path)
            print(result)

    except (KeyError, TypeError, IndexError):
        print("Encerrando script\n")
        raise ValueError("Opção inválida\n")
    finally:
        print("Encerrando script\n")


def create_news():
    with open("correct.csv"):
        pass
    pass


# analyzer_menu()