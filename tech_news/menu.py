import sys
from tech_news.collector.importer import csv_importer
from tech_news.database import create_news


def collector_menu():
    print("Selecione uma das opções a seguir:\n " +
          "1 - Importar notícias a partir de um arquivo CSV;\n " +
          "2 - Exportar notícias para CSV;\n " +
          "3 - Raspar notícias online;\n " +
          "4 - Sair."
          )
    user_input = input()
    if first_input_step(user_input) == "Opção inválida\n":
        sys.stderr.write("Opção inválida\n")
    else:
        return first_input_step(user_input)


def analyzer_menu():
    """Seu código deve vir aqui"""


def first_input_step(argument):
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
        print(result)


def second_function_step(argument):
    switcher = {
        "1": import_from_csv_and_save_in_database(argument)
    }
    return (switcher.get(argument))


def import_from_csv_and_save_in_database(argument):
    data_from_csv = csv_importer(argument)
    create_news(data_from_csv)
