import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            read = csv.reader(file, delimiter=";")
            dictInfo = {key: [] for key in read}
            for value in dictInfo:
                dictInfo['key'].append(value)
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        return read
    finally:
        print("deu certo")


csv_importer('correct.csv')

