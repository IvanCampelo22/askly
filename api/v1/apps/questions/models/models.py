from sqlalchemy import Integer, String, Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Text(Base):
    __tablename__ = 'text'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('survey.id', ondelete='CASCADE'), nullable=False)
    order = Column(Integer, nullable=False)
    type = Column(String(320), nullable=False)
    input_type = Column(String(320), nullable=False)
    text = Column(String, nullable=False)

    _survey = relationship('Survey', back_populates='_text')

class Scale(Base):
    __tablename__ = 'scale'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('survey.id', ondelete='CASCADE'), nullable=False)
    order = Column(Integer, nullable=False)
    type = Column(String(320), nullable=False)
    input_type = Column(String(320), nullable=False)
    text = Column(String, nullable=False)
    scale_min = Column(Integer, nullable=False)
    scale_max = Column(Integer, nullable=False)

    _survey = relationship('Survey', back_populates='_scale')

class MultipleChoice(Base):
    __tablename__ = 'multiple_choice'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('survey.id', ondelete='CASCADE'), nullable=False)
    order = Column(Integer, nullable=False)
    type = Column(String(320), nullable=False)
    input_type = Column(String(320), nullable=False)
    text = Column(String, nullable=False)

    _survey = relationship('Survey', back_populates='_multiple_choices')
    _multiple_question_multi = relationship('MultiQuestionMulti', back_populates='_multiple_choices')
    

class SingleChoice(Base):
    __tablename__ = 'single_choice'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('survey.id', ondelete='CASCADE'), nullable=False)
    order = Column(Integer, nullable=False)
    type = Column(String(320), nullable=False)
    input_type = Column(String(320), nullable=False)
    text = Column(String, nullable=False)

    _survey = relationship('Survey', back_populates='_single_choices')
    _single_question_multi = relationship('MultiQuestionSingle', back_populates='_single_choices')

class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('survey.id', ondelete='CASCADE'), nullable=False)
    order = Column(Integer, nullable=False)
    type = Column(String(320), nullable=False)
    input_type = Column(String(320), nullable=False)
    text = Column(String, nullable=False)

    _survey = relationship('Survey', back_populates='_email')

class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('survey.id', ondelete='CASCADE'), nullable=False)
    order = Column(Integer, nullable=False)
    type = Column(String(320), nullable=False)
    input_type = Column(String(320), nullable=False)
    text = Column(String, nullable=False)

    _survey = relationship('Survey', back_populates='_document')


class MultiQuestionMulti(Base):
    __tablename__ = 'multi_question_multi'

    id = Column(Integer, primary_key=True, index=True)
    multi_choice_id = Column(Integer, ForeignKey('multiple_choice.id', ondelete='CASCADE'), nullable=True)
    text = Column(String, nullable=False)

    _multiple_choices = relationship('MultipleChoice', back_populates='_multiple_question_multi')


class MultiQuestionSingle(Base):
    __tablename__ = 'multi_question_single'

    id = Column(Integer, primary_key=True, index=True)
    single_choice_id = Column(Integer, ForeignKey('single_choice.id', ondelete='CASCADE'), nullable=True)
    text = Column(String, nullable=False)

    _single_choices = relationship('SingleChoice', back_populates='_single_question_multi')
