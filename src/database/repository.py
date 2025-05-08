from sqlalchemy.orm import Session
from src.database.models import PageEvent

def insert_page_event(session: Session, payload: dict):
    event = PageEvent(**payload)
    session.add(event)
    session.commit()
    return
