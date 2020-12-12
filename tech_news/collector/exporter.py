import csv
from os import path


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath) as file:
        csv.writer(delimiter=";", quotechar='"')
