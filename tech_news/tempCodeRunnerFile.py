 if user_input == 1:
        file = input("Digite o nome do arquivo CSV a ser importado: ")
        return csv_importer(file)
    elif user_input == 2:
        file = input("Digite o nome do arquivo CSV a ser exportado: ")
        return csv_exporter(file)
    elif user_input == 3:
        pages = input("Digite a quantidade de páginas a serem raspadas: ")
        return scrape(fetch_content, pages)
    elif user_input == 4:
        return print("Encerrando script")
    else:
        return print("Opção inválida")