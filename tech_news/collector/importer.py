import csv

HEADER = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
]


def validFile(file):
    if not file.endswith(".csv"):
        raise ValueError("Formato invalido")
    return file.split("/")[-1]


def csv_importer(filepath):
    file_name = validFile(filepath)
    try:
        with open(filepath, "r") as file:
            read = csv.DictReader(file, delimiter=";")

            if read.fieldnames != HEADER:
                raise ValueError("Headers invalidos")

            file_read = [
                {key: value for key, value in line.items()} for line in read
            ]

    except FileNotFoundError:
        raise ValueError(f"Arquivo {file_name} não encontrado")
    else:
        return file_read
