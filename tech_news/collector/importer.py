import csv
from os import path


def csv_importer(filepath):
    news_list = []
    if not filepath.endswith('csv'):
        raise(ValueError("Formato invalido"))

    if not path.exists(filepath):
        raise(ValueError(
            f"Arquivo {path.basename(filepath)} não encontrado")
        )

    with open(filepath, "r") as file:
        get_news_list = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = get_news_list

        for news in data:
            news_list.append({
                "url": news[0],
                "title": news[1],
                "timestamp": news[2],
                "writer": news[3],
                "shares_count": news[4],
                "comments_count": news[5],
                "summary": news[6],
                "sources": news[7],
                "categories": news[8],
            })
    return news_list
