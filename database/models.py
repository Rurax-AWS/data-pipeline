from sqlalchemy import Column, Integer, Text, TIMESTAMP, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PageEvent(Base):
    __tablename__ = 'page_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_event = Column(Text)
    ga_id = Column(Text)
    user_id = Column(Text)
    item_id = Column(Text)
    item_type = Column(Text)
    page_ref = Column(Text)
    tags = Column(Text)
    add_cart_item_ids = Column(Text)
    add_coment_comment = Column(Text)
    carr_img_display_img_ref = Column(Text)
    carr_img_display_pos = Column(Integer)
    carr_img_view_img_ref = Column(Text)
    carr_img_view_pos = Column(Integer)
    category_click_category = Column(Text)
    index_search_category = Column(Text)
    index_search_search = Column(Text)
    page_search_search = Column(Text)
    page_search_filter = Column(Text)
    item_display_pos = Column(Text)
    item_view_pos = Column(Text)
    item_rtime_time = Column(Integer)
    event_time = Column(TIMESTAMP)
    event_ingest = Column(TIMESTAMP)
    data = Column(JSON)
    item_click_title = Column(Text)
    carr_click = Column(Text)
    contact = Column(Text)
