import boto3
from botocore.exceptions import BotoCoreError, ClientError

def upload_to_s3(bucket_name, object_name, file_content, extra_args=None,):
    
    try:
        s3_client = boto3.client('s3', 'us-east-1')
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=file_content,
            **(extra_args or {})
        )
        print(f"Arquivo {object_name} salvo Com sucesso.")
        return True
    except (BotoCoreError, ClientError) as error:
        print(f"Erro ao salvar o arquivo: {error}")
        return False