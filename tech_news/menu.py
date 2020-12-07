from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.ratings import top_5_news, top_5_categories
# Fazendo em apenas uma linha não passou no teste
from tech_news.analyzer import search_engine
import sys

# Use tech-news-collector ou -analyzer p/ rodar estes programas direto do shell

col_menu = """Selecione uma das opções a seguir:

1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Raspar notícias online;
4 - Sair.
"""

alz_menu = """Selecione uma das opções a seguir:

1 - Buscar notícias por título;
2 - Buscar notícias por data;
3 - Buscar notícias por fonte;
4 - Buscar notícias por categoria;
5 - Listar top 5 notícias;
6 - Listar top 5 categorias;
7 - Sair.
"""


def collector_menu():
    user_choice = int(input(col_menu))
    if user_choice == 1:
        path = input('Digite o nome do arquivo CSV a ser importado:')
        return csv_importer(path)
    elif user_choice == 2:
        path = input('Digite o nome do arquivo CSV a ser exportado:')
        return csv_exporter(path)
    elif user_choice == 3:
        pages = input(
            'Digite a quantidade de páginas a serem raspadas:'
            )
        return scrape(fetcher=fetch_content, pages=int(pages))
    elif user_choice == 4:
        print('Encerrando script\n')
        exit
    else:
        sys.stderr.write('Opção inválida\n')


def analyzer_menu():
    user_choice = int(input(alz_menu))
    if user_choice == 1:
        path = input('Digite o título:')
        return search_engine.search_by_title(path)
    elif user_choice == 2:
        path = input('Digite a data no formato aaaa-mm-dd:')
        return search_engine.search_by_date(path)
    elif user_choice == 3:
        pages = input('Digite a fonte:')
        return search_engine.search_by_source(int(pages))
    elif user_choice == 4:
        pages = input('Digite a categoria:')
        return search_engine.search_by_category(int(pages))
    elif user_choice == 5:
        return top_5_news()
    elif user_choice == 6:
        return top_5_categories()
    elif user_choice == 7:
        print('Encerrando script\n')
        exit
    else:
        sys.stderr.write('Opção inválida\n')
