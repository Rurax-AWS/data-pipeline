import json
from utils.sqs_client import receive_messages, process_message, delete_message
from utils.csv_convert import json_to_csv
from utils.s3_client import upload_to_s3
import os

def event_pubsub_subscribe(event, context):
    print("Verificando mensagens na fila SQS...")

    # Configurações do S3
    bucket_name = os.getenv("S3_BUCKET_BACKUP")

    while True:
        messages = receive_messages(10)
        if not messages:
            print("Nenhuma mensagem disponível na fila.")
            break

        for message in messages:
            # Processa a mensagem
            process_message(message)

            # Converte a mensagem para CSV
            data = [json.loads(message['Body'])]  # Envolvendo a mensagem em uma lista
            file_name, csv_content = json_to_csv(data)

            print(f"CSV gerado: {file_name}")

            # Faz o upload do CSV para o S3
            success = upload_to_s3(
                bucket_name=bucket_name,
                object_name=file_name,
                file_content=csv_content,  # Passa o conteúdo do CSV diretamente
                extra_args={"ContentType": "text/csv"}  # Define o tipo de conteúdo
            )

            # Deleta a mensagem da fila
            delete_message(message['ReceiptHandle'])

    return "Todas as mensagens foram processadas com sucesso."