import csv
from database import find_news


def exporter_support(data, file):
    for document in data:
        for key in document:
            if isinstance(document[key], list):
                document[key] = ",".join(document[key])
    header = list(data[0].keys())
    csv_writer = csv.DictWriter(file, header, delimiter=";")
    csv_writer.writeheader()
    csv_writer.writerows(data)


def csv_exporter(filepath):
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath, "w") as file:
            data = find_news()
            exporter_support(data, file)
    except ValueError:
        raise ValueError("Formato invalido")
