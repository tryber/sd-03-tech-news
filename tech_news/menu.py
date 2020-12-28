import sys



def collector_menu():
    print("Selecione uma das opções a seguir:\n " +
          "1 - Importar notícias a partir de um arquivo CSV;\n " +
          "2 - Exportar notícias para CSV;\n " +
          "3 - Raspar notícias online;\n " +
          "4 - Sair."
          )
    user_input = input()
    print(switch_demo(user_input))


def analyzer_menu():
    """Seu código deve vir aqui"""


def switch_demo(argument):
    # https://jaxenter.com/implement-switch-case-statement-python-138315.html
    switcher = {
         "1": "January",
         "2": "February",
         "3": "March",
         "4": "Encerrando script\n"
    }
    return (switcher.get(argument, sys.stderr.write("Opção inválida\n")))
