import json 
from utils.sqs_client import receive_messages, process_message, delete_message
from utils.csv_convert import json_to_csv
from utils.s3_client import upload_to_s3

def event_pubsub_subscribe(event, context):
    print("Verificando mensagens na fila SQS...")

    # Defina o prefixo para o caminho no S3
    prefix = "datasets/test"

    while True:
        messages = receive_messages(10)
        if not messages:
            print("Nenhuma mensagem disponível na fila.")
            break

        for message in messages:
            # Processa a mensagem
            process_message(message)

            # Converte a mensagem para CSV e salva uma cópia local
            data = [json.loads(message['Body'])]  # Envolvendo a mensagem em uma lista
            file_name, csv_content = json_to_csv(data, prefix)

            print(f"CSV gerado: {file_name}")

            # Deleta a mensagem da fila
            delete_message(message['ReceiptHandle'])

    return "Todas as mensagens foram processadas com sucesso."