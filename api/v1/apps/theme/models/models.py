from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from api.v1.apps.survey.models.models import Survey
from db.session import Base
import datetime


class Theme(Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(320), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    created_at = Column(DateTime, default=datetime.datetime.now)

    _survey = relationship('Survey', back_populates='_theme')
