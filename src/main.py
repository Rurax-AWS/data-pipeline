from src.utils.sqs_client import receive_messages, process_message, delete_message
from src.utils.csv_convert import json_to_csv
from src.utils.s3_client import upload_to_s3
from src.database.db_client import insert_page_event
import os
from time import gmtime, strftime, sleep

def event_pubsub_subscribe(event, context):
    print("Verificando mensagens na fila SQS...")

    bucket_name = os.getenv("S3_BUCKET_BACKUP")

    while True:
        messages = receive_messages(10)
        if not messages:
            print("Nenhuma mensagem disponível na fila.")
            break

        for message in messages:

            getgmtime = gmtime()
            
            timestamp_event_ingest = strftime("%Y-%m-%d %H:%M:%S", getgmtime)  
            timestamp_csv = strftime("%Y%m%d_%H%M%S", getgmtime)

            body = process_message(message, timestamp_event_ingest)

            insert_page_event(body)

            data = [body]
            file_name, csv_content = json_to_csv(data, timestamp_csv)

            upload_to_s3(
                bucket_name=bucket_name,
                object_name=file_name,
                file_content=csv_content, 
                extra_args={"ContentType": "text/csv"}
            )

            delete_message(message['ReceiptHandle'])

            sleep(3)

    return "Todas as mensagens foram processadas com sucesso."