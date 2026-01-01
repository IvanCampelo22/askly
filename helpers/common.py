from typing import Any, Dict
from sqlalchemy.orm import selectinload
from api.v1.apps.survey.models.models import Survey
from api.v1.apps.questions.models.models import SingleChoice, MultipleChoice
from api.v1.apps.theme.models.models import Theme
from sqlalchemy.future import select


async def validate_and_update(db_object: Any, **kwargs):
    """
    Validates and updates a database object, setting non-None values.

    Args:
        db_object (Any): The database object to update.
        kwargs (dict): Keyword arguments containing key-value pairs for update.

    Raises:
        TypeError: If `db_object` is not an instance of a supported class.
    """
    if not isinstance(db_object, (Survey, SingleChoice, MultipleChoice, Theme)):
        raise TypeError("validate_and_update only works with Survey, SingleChoice, or MultipleChoice instances")

    for key, value in kwargs.items():
        if value is not None:
            setattr(db_object, key, value)


async def get_one_and_filter_survey(session, survey_obj: Any, param = Any) -> Dict:
    """
    Fetches and filters a single survey with eager loading of related questions.

    Args:
        session (sqlalchemy.ext.asyncio.AsyncSession): The SQLAlchemy session object.
        survey_obj (Any): The model class representing the survey (e.g., Survey).
        param (Any): The filter parameter value.

    Returns:
        Dict: A dictionary containing survey data, including questions.

    Raises:
        sqlalchemy.orm.exc.NoResultFound: If no survey matching the filter is found.
    """


    query = select(Survey).where(survey_obj == param).options(
        selectinload(Survey._text),
        selectinload(Survey._scale),
        selectinload(Survey._single_choices).options(
            selectinload(SingleChoice._single_question_multi)
        ),
        selectinload(Survey._multiple_choices).options(
            selectinload(MultipleChoice._multiple_question_multi)
        ),
        selectinload(Survey._email),
        selectinload(Survey._document)
    )
    
    result = await session.execute(query)
    survey = result.scalars().one()
    
    questions = sorted(
        survey._text + survey._scale + survey._single_choices + survey._multiple_choices + survey._email + survey._document,
        key=lambda q: q.order
    )
    
    survey_data = {
        "id": survey.id,
        "title": survey.title,
        "description": survey.description,
        "questions": []
    }
    
    for question in questions:
        question_data = {
            "id": question.id,
            "type": question.type,
            "text": question.text,
            "input_type": getattr(question, 'input_type', None),
            "order": question.order
        }
        
        if question.type == 'single_choice':
            question_data["single_question_multi"] = [
                {
                    "id": sqm.id,
                    "text": sqm.text
                }
                for sqm in question._single_question_multi
            ] if hasattr(question, '_single_question_multi') else []

        elif question.type == 'multiple_choice':
            question_data["multiple_question_multi"] = [
                {
                    "id": mqm.id,
                    "text": mqm.text
                }
                for mqm in question._multiple_question_multi
            ] if hasattr(question, '_multiple_question_multi') else []

        survey_data["questions"].append(question_data)
    
    return survey_data