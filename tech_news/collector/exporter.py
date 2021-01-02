from tech_news.database import db
import csv


def get_db_data():
    return db.news.find()


def csv_translate(data, output_file):
    data = [doc for doc in data]
    for doc in data:
        del doc["_id"]
        for field in doc:
            print(type(doc[field]))
            if isinstance(doc[field], list):
                doc[field] = ",".join(doc[field])
    header = list(data[0].keys())
    dict_writer = csv.DictWriter(output_file, header, delimiter=";")
    dict_writer.writeheader()
    dict_writer.writerows(data)

    return dict_writer


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    try:
        if not filepath.endswith(".csv"):
            raise ValueError()
        with open(filepath, "w") as file:
            data = get_db_data()
            print(data)
            csv_translate(data, file)
    except ValueError:
        raise ValueError("Formato invalido")
