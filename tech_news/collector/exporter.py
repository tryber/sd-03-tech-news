import csv


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    with open(filepath) as file:
        raw_csv = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = raw_csv
        return {header: data}
