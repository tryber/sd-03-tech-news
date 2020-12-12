import csv
from os import path


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    exists = path.exists(filepath)
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    if not exists:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
    with open(filepath) as file:
        raw_csv = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = raw_csv
        data_len, header_len = len(data), len(header)
        news, temp = [], {}
        for i in range(data_len):
            for j in range(header_len):
                temp[header[j]] = data[i][j]
            news.append(temp)
            temp = {}
        return news


if __name__ == "__main__":
    print(csv_importer('./correc.csv'))
