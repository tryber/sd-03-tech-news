import csv

news_list = []


def csv_importer(filepath):
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            header, *content = csv.reader(file, delimiter=";")
            for info in content:
                news_list.append({
                    "url": info[0],
                    "title": info[1],
                    "timestamp": info[2],
                    "writer": info[3],
                    "shares_count": info[4],
                    "comments_count": info[5],
                    "summary": info[6],
                    "sources": info[7],
                    "categories": info[8],
                })
        return news_list
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
