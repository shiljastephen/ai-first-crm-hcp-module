from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(255))

    interaction_type = Column(String(100))

    interaction_date = Column(Date)

    interaction_time = Column(Time)

    attendees = Column(Text)

    topics_discussed = Column(Text)

    materials_shared = Column(Text)

    summary = Column(Text)

    sentiment = Column(String(100))

    follow_up = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)