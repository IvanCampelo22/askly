from pydantic import BaseModel
from api.v1.apps.questions.schemas.schemas import ScaleSchema, TextSchema, MultipleChoice, SingleChoice, EmailSchema, DocumentSchema
from typing import List, Union

class SurveySchema(BaseModel):
    id: int 
    title: str = ''
    description: str = ''
    options: List[Union[ScaleSchema, TextSchema, MultipleChoice, SingleChoice, EmailSchema, DocumentSchema]]