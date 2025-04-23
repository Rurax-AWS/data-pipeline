import csv
import os
from time import gmtime, strftime
from io import StringIO

def json_to_csv(data):

    time_now = strftime("%Y%m%d_%H%M%S", gmtime())
    file_name = f"{time_now}.csv"  

    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    return file_name, csv_buffer.getvalue()