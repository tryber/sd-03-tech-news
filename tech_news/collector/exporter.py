import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    news = find_news()
    header = list(news[0].keys())
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)
        rows = []
        for new in news:
            temp = []
            for elem in list(new.values()):
                if isinstance(elem, list):
                    espacer = ','
                    new_elem = espacer.join(elem)
                    temp.append(new_elem)
                else:
                    temp.append(elem)
            rows.append(temp)
            temp = []
        writer.writerows(rows)


if __name__ == "__main__":
    csv_exporter("a.csv")
