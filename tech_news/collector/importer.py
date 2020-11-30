import csv

baseArr = [
    "categories",
    "comments_count",
    "shares_count",
    "sources",
    "summary",
    "timestamp",
    "title",
    "url",
    "writer",
]


def csv_importer(filepath):
    arr = []
    try:
        if filepath[-4:] != ".csv":
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            result = csv.reader(file, delimiter=";", quotechar='"')
            header, *data = result
            header.sort()
            if header != baseArr:
                raise ValueError("Formato invalido aqui")
            for row in data:
                url, title, timestamp, writer, shares_count, *second_half = row
                comments_count, summary, sources, categories = second_half
                arr.append(
                    {
                        "url": url,
                        "title": title,
                        "timestamp": timestamp,
                        "writer": writer,
                        "shares_count": shares_count,
                        "comments_count": comments_count,
                        "summary": summary,
                        "sources": sources,
                        "categories": categories,
                    }
                )
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
    else:
        return arr


print(csv_importer("correct.csv"))
