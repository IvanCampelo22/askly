from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UUID, Boolean
from sqlalchemy.orm import relationship
from db.session import Base
import datetime
import uuid

class Survey(Base):
    __tablename__ = 'survey'

    id = Column(Integer, primary_key=True, index=True)
    theme_id = Column(Integer, ForeignKey('theme.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    identifier_code = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String(320), nullable=False, unique=True)
    description = Column(String(520), nullable=False)
    version = Column(Integer, nullable=False, default=0)
    answered = Column(Boolean, nullable=False, default=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    created_at = Column(DateTime, default=datetime.datetime.now)

    _users = relationship('Users', back_populates='_survey')

    _theme = relationship('Theme', back_populates='_survey')
    _text = relationship('Text', back_populates='_survey', cascade="all, delete-orphan", passive_deletes=True)
    _scale = relationship('Scale', back_populates='_survey', cascade="all, delete-orphan", single_parent=True, passive_deletes=True)    
    _multiple_choices = relationship('MultipleChoice', back_populates='_survey', cascade="all, delete-orphan", passive_deletes=True)
    _single_choices = relationship('SingleChoice', back_populates='_survey', cascade="all, delete-orphan", passive_deletes=True)
    _email = relationship('Email', back_populates='_survey', cascade="all, delete-orphan", passive_deletes=True)
    _document = relationship('Document', back_populates='_survey', cascade="all, delete-orphan", passive_deletes=True)
    