import csv
from io import StringIO

def json_to_csv(data, timestamp):
    """
    Converte JSON para CSV e retorna o nome do arquivo e o conteúdo CSV.

    Args:
        data (list of dict): Lista de dicionários a serem convertidos para CSV.
        timestamp (str): Timestamp único para o nome do arquivo.

    Returns:
        tuple: (nome_do_arquivo, conteúdo_csv)
    """
    file_name = f"{timestamp}.csv"  # Nome do arquivo com o timestamp

    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    return file_name, csv_buffer.getvalue()