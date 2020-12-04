import csv


dic = {
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
}


def validFile(file):
    if not file.endswith(".csv"):
        raise ValueError("Formato invalido")
    return file.split("/")[-1]


def csv_importer(filepath):
    validFile(filepath)
    try:
        with open(filepath, "r") as file:
            read = csv.DictReader(file, delimiter=";")
            if read.fieldnames != dic:
                raise ValueError("Headers invalidos")
            file_read = [
                {key: value for key, value in line.items()} for line in read
            ]
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        return file_read
    finally:
        print("deu certo")


# csv_importer('correct.csv')

# with open(, 'w') as file:
#             csv_writer = DictWriter(file, fieldnames=data[0].keys())
#             csv_writer.writeheader()
#             for item in data:
#                 csv_writer.writerow(item)
# data = [    {key: value for key, value in line.items()} for line in data    ]
# with open(filepath) as file:
#             read = csv.reader(file, delimiter=";")
#             dictInfo = {key: [] for key in read}
#             for value in dictInfo.items():
#                 dictInfo['key'].append(value)
