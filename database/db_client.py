import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import PageEvent

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def convert_keys_to_lowercase(data: dict) -> dict:
    """Converte todas as chaves para minúsculas e renomeia 'type' para 'type_event'."""
    converted = {}
    for k, v in data.items():
        key_lower = k.lower()
        if key_lower == "type":
            converted["type_event"] = v
        else:
            converted[key_lower] = v
    return converted


def insert_page_event_record(session, data: dict):
    try:
        # Converte e ajusta chaves
        data = convert_keys_to_lowercase(data)

        # Cria o evento
        event = PageEvent(**data)
        session.add(event)
        session.commit()
        return event.id
    except Exception as e:
        session.rollback()
        print(f"Erro ao inserir evento: {e}")
        raise

def insert_page_event(data: dict):
    with SessionLocal() as session:
        insert_page_event_record(session, data)
    print("Mensagem salva no banco.")
