from utils.sqs_client import receive_messages, process_message, delete_message

def event_pubsub_subscribe(event, context):
    # print("Verificando mensagens na fila SQS...")

    while True:
        messages = receive_messages(10)
        if not messages:
            # print("Nenhuma mensagem disponível na fila.")
            break

        for message in messages:
            # print(f"Processando mensagem: {message['MessageId']}")
            process_message(message)
            delete_message(message['ReceiptHandle'])

    return "Todas as mensagens foram processadas com sucesso."