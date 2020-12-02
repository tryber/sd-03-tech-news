import csv

spected_headers = [
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


def filepath_if_is_valid(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    return filepath.split("/")[-1]


def csv_importer(filepath):
    filename = filepath_if_is_valid(filepath)
    try:
        with open(filepath, "r") as file:
            data = csv.DictReader(file, delimiter=";")

            if data.fieldnames != spected_headers:
                raise ValueError("Headers invalidos")

            file_data = [
                {key: value for key, value in line.items()} for line in data
            ]

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filename} não encontrado")
    else:
        return file_data
