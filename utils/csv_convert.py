import csv
from io import StringIO

def json_to_csv(data, timestamp):
    file_name = f"{timestamp}.csv" 

    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    print(f"Backup {file_name} criado com sucesso.")

    return file_name, csv_buffer.getvalue()