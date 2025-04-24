import os
import boto3
from time import gmtime, strftime
import json

sqs = boto3.client('sqs', region_name='us-east-1')
queue_url = os.environ['SQS_QUEUE_URL']

def receive_messages(max_messages=10):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=max_messages,
        WaitTimeSeconds=10
    )
    return response.get('Messages', [])

def process_message(message, timestamp_event_ingest):
    body = json.loads(message['Body'])
    body['EVENT_INGEST'] = timestamp_event_ingest
    print("Mensagem processada:", json.dumps(body, indent=4))

    return body

def delete_message(receipt_handle):
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print(f"Mensagem deletada da fila com sucesso.")
