from sqlalchemy import Column, Integer, String, DateTime, UUID
from db.session import Base
import datetime
import uuid

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, index=True)
    client_code = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String(320), nullable=False, unique=True)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    created_at = Column(DateTime, default=datetime.datetime.now)
