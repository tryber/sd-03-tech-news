import sys
from tech_news.collector.importer import csv_importer
from tech_news.database import create_news
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.search_engine import (search_by_title,
                                              search_by_date,
                                              search_by_source,
                                              search_by_category
                                              )


def collector_menu():
    print("Selecione uma das opções a seguir:\n " +
          "1 - Importar notícias a partir de um arquivo CSV;\n " +
          "2 - Exportar notícias para CSV;\n " +
          "3 - Raspar notícias online;\n " +
          "4 - Sair."
          )
    user_input = input()
    if first_input_step_collector(user_input) == "Opção inválida\n":
        sys.stderr.write("Opção inválida\n")
    elif first_input_step_collector(user_input) == "Encerrando script\n":
        print("Encerrando script\n")
    else:
        print(first_input_step_collector(user_input))
        user_input2 = input()
        print(second_function_step_collector(user_input, user_input2))


def analyzer_menu():
    print("Selecione uma das opções a seguir:\n " +
          "1 - Buscar notícias por título;\n " +
          "2 - Buscar notícias por data;\n " +
          "3 - Buscar notícias por fonte;\n " +
          "4 - Buscar notícias por categoria;\n " +
          "5 - Listar top 5 notícias;\n " +
          "6 - Listar top 5 categorias;\n " +
          "7 - Sair.")
    user_input = input()
    if first_input_step_analyzer(user_input) == "Opção inválida\n":
        sys.stderr.write("Opção inválida\n")
    elif first_input_step_analyzer(user_input) == "Encerrando script\n":
        print("Encerrando script\n")
    else:
        print(first_input_step_analyzer(user_input))
        user_input2 = input()
        print(second_function_step_analyzer(user_input, user_input2))


def first_input_step_collector(argument):
    # https://jaxenter.com/implement-switch-case-statement-python-138315.html
    switcher = {
         "1": "January",
         "2": "February",
         "3": "March",
         "4": "Encerrando script\n"
    }
    result = switcher.get(argument, "Opção inválida\n")
    if result == "Opção inválida\n":
        return "Opção inválida\n"
    else:
        return result


def second_function_step_collector(argument, argument2):
    if argument == "1":
        return import_from_csv_and_save_in_database(argument2)
    elif argument == "2":
        return csv_exporter(argument2)
    elif argument == "3":
        return create_news(scrape(fetcher=fetch_content, pages=1))


def import_from_csv_and_save_in_database(argument):
    data_from_csv = csv_importer(argument)
    create_news(data_from_csv)


def first_input_step_analyzer(argument):
    # https://jaxenter.com/implement-switch-case-statement-python-138315.html
    switcher = {
         "1": "January",
         "2": "February",
         "3": "March",
         "4": "category",
         "5": "top noticias",
         "6": "top categorias",
         "7": "Encerrando script\n"
    }
    result = switcher.get(argument, "Opção inválida\n")
    if result == "Opção inválida\n":
        return "Opção inválida\n"
    else:
        return result


def second_function_step_analyzer(argument, argument2):
    if argument == "1":
        return search_by_title(argument2)
    elif argument == "2":
        return search_by_date(argument2)
    elif argument == "3":
        return search_by_source(argument2)
    elif argument == "4":
        return search_by_category(argument2)
