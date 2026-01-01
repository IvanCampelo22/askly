from pydantic import BaseModel
from typing import List


class MultiQuestionSingleSchema(BaseModel):
    id: int
    text: str = ''

class MultiQuestionMultipleSchema(BaseModel):
    id: int
    text: str = ''

class ScaleSchema(BaseModel):
    id: int
    type: str = 'nps'
    input_type: str = 'scale'
    text: str = ''
    scale_min: int = 0
    scale_max: int = 10

class SingleChoice(BaseModel):
    id: int
    type: str = 'single_choice'
    input_type: str = 'radio'
    text: str = ''
    options: List[MultiQuestionSingleSchema]

class MultipleChoice(BaseModel):
    id: int
    type: str = 'multiple_choice'
    input_type: str = 'checkbox'
    text: str = ''
    options: List[MultiQuestionMultipleSchema]

class TextSchema(BaseModel):
    id: int
    type: str = 'text'
    input_type: str = 'textarea'
    text: str = ''

class DocumentSchema(BaseModel):
    id: int
    type: str = 'document'
    input_type: str = 'document'
    text: str = ''

class EmailSchema(BaseModel):
    id: int
    type: str = 'email'
    input_type: str = 'email'
    text: str = ''