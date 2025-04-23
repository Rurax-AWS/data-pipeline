import json
from utils.sqs_client import receive_messages, process_message, delete_message
from utils.csv_convert import json_to_csv
from utils.s3_client import upload_to_s3
import os
from time import gmtime, strftime

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
            # Gera o timestamp único

            getgmtime = gmtime()
            
            timestamp_event_ingest = strftime("%Y-%m-%d %H:%M:%S", getgmtime)  
            timestamp_csv = strftime("%Y%m%d_%H%M%S", getgmtime)

            # Processa a mensagem e adiciona o timestamp no EVENT_INGEST
            body = json.loads(message['Body'])
            body['EVENT_INGEST'] = timestamp_event_ingest
            print("Mensagem processada:", json.dumps(body, indent=4))

            # Converte a mensagem para CSV
            data = [body]  # Envolvendo a mensagem em uma lista
            file_name, csv_content = json_to_csv(data, timestamp_csv)

            print(f"CSV gerado: {file_name}")

            # Faz o upload do CSV para o S3
            success = upload_to_s3(
                bucket_name=bucket_name,
                object_name=file_name,
                file_content=csv_content,  # Passa o conteúdo do CSV diretamente
                extra_args={"ContentType": "text/csv"}  # Define o tipo de conteúdo
            )

            if success:
                print(f"Arquivo enviado com sucesso para o S3: s3://{bucket_name}/{file_name}")
            else:
                print(f"Falha ao enviar o arquivo para o S3: {file_name}")

            # Deleta a mensagem da fila
            delete_message(message['ReceiptHandle'])

    return "Todas as mensagens foram processadas com sucesso."