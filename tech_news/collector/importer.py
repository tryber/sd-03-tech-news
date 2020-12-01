import csv


def csv_importer(filepath):
    try:
        with open(filepath) as file:
            writer = csv.reader(file, delimiter=",", quotechar='"')
            writer.writerow(
                [
                    "url",
                    "title",
                    "timestamp",
                    "writer",
                    "shares_count",
                    "comments_count",
                    "summary",
                    "sources",
                    "categories",
                ]
            )
        # if not filepath or filepath.endswith(".csv"):
        #     raise ValueError("Formato inválido")
    except ValueError:
        return ""
    else:
        return writer
        # for content in filepath.items():
        #     writer.writerow(content)
    finally:
        print('deu certo')
