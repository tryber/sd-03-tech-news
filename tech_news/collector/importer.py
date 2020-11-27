import csv

EXP_HEADERS = [
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


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath, "r") as file:
            data = csv.DictReader(file, delimiter=";")
            if data.fieldnames != EXP_HEADERS:
                raise ValueError("Headers invalidos")
            info = [
                {key: value for key, value in line.items()} for line in data
            ]

    except FileNotFoundError:
        print(f"############################# {filepath}")
        filename = filepath.split("/")[-1]
        raise ValueError(f"Arquivo {filename} não encontrado")
    else:
        return info


csv_importer("correct.csv")
