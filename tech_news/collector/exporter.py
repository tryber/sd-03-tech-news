import csv
from tech_news.database import find_news
# csv_exporter('./samples/saveddata.csv') para testar


def csv_exporter(filepath):
    if not filepath.endswith('.csv'):
        raise ValueError('\nFormato invalido')

    # O parâmetro w já sobrescreve quaisquer arquivos de o mesmo nome
    # já existentes. Caso queiramos um erro nesse caso, é só usar o 'x'
    with open(filepath, 'w') as file:
        write_buffer = csv.writer(file, delimiter=';', quotechar='"')

        header = [
            'url',
            'title',
            'timestamp',
            'writer',
            'shares_count',
            'comments_count',
            'summary',
            'sources',
            'categories',
        ]
        write_buffer2 = csv.DictWriter(
            file,
            fieldnames=header,
            delimiter=';',
            quotechar='"'
        )

        # Inserindo o cabeçalho antes
        write_buffer.writerow(header)
        # Puxando do banco as notícias
        news_dump = find_news()

        # Gravando linha a linha cada notícia
        for news in news_dump:
            print(news)
            write_buffer2.writerow(news)
        file.close()
