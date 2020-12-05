import csv

def csv_importer(filepath):
    with open(filepath) as file:
        arquivo = csv.reader(file, delimiter=";")
        header, *data = arquivo
        
