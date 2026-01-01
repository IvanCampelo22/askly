from sqlalchemy import Column, Integer, String, DateTime,Boolean
from db.session import Base
import datetime
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(520), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    _survey = relationship('Survey', back_populates='_users', cascade="all, delete-orphan", passive_deletes=True)
