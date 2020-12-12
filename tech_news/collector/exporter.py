import csv
from pymongo import MongoClient


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    client = MongoClient()
    db = client.tech_news
    news = db.news.find()
    header = list(news[0].keys())[1:]
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)
        rows = []
        for new in news:
            temp = []
            for elem in list(new.values())[1:]:
                if isinstance(elem, list):
                    espacer = ','
                    new_elem = espacer.join(elem)
                    temp.append(new_elem)
                else:
                    temp.append(elem)
            rows.append(temp)
            temp = []
        writer.writerows(rows)
    client.close()


if __name__ == "__main__":
    csv_exporter("a.csv")
