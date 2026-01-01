from helpers.new_and_update import new_scale_for_update, new_text_for_update, new_email_for_update, new_document_for_update, new_multiple_choice_for_update, new_single_choice_for_update
from api.v1.apps.questions.models.models import SingleChoice, MultipleChoice, Text, Scale, Email, Document
from helpers.common import get_one_and_filter_survey
from api.v1.apps.survey.models.models import Survey
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import async_session
from sqlalchemy.future import select
from typing import Dict, Any, List


@async_session
async def get_one(session: AsyncSession, survey_id):
    """Pega um formulário pelo identificador"""

    survey_data = await get_one_and_filter_survey(session=session, survey_obj=Survey.id, param=survey_id)
    return survey_data
    
@async_session
async def update(session: AsyncSession, survey_id: int, questions_data: List[dict], **kwargs) -> Any:
    """Atualiza formulários e cria uma nova versão com perguntas do tipo Scale"""

    result_survey = await session.execute(select(Survey).where(Survey.id == survey_id))
    existing_survey = result_survey.scalars().first()

    if not existing_survey:
        raise ValueError("Formulário não encontrado ou já foi respondido")

    result_scale = await session.execute(select(Scale).where(Scale.survey_id == survey_id))
    existing_scales = result_scale.scalars().all()

    result_text = await session.execute(select(Text).where(Text.survey_id == survey_id))
    existing_texts = result_text.scalars().all()

    result_email = await session.execute(select(Email).where(Email.survey_id == survey_id))
    existing_emails = result_email.scalars().all()

    result_document = await session.execute(select(Document).where(Document.survey_id == survey_id))
    existing_documents = result_document.scalars().all()

    result_multiple_choice = await session.execute(select(MultipleChoice).where(MultipleChoice.survey_id == survey_id))
    existing_multiple_choices = result_multiple_choice.scalars().all()

    result_single_choice = await session.execute(select(SingleChoice).where(SingleChoice.survey_id == survey_id))
    existing_single_choices = result_single_choice.scalars().all()

    new_survey = Survey(
        version=existing_survey.version + 1,
        **{key: kwargs.get(key, getattr(existing_survey, key)) for key in kwargs}
    )
    session.add(new_survey)
    await session.flush()

    await new_scale_for_update(session=session, existing_scales=existing_scales, questions_data=questions_data, new_survey=new_survey)    
    await new_text_for_update(session=session, existing_texts=existing_texts, questions_data=questions_data, new_survey=new_survey)
    await new_email_for_update(session=session, existing_emails=existing_emails, questions_data=questions_data, new_survey=new_survey)
    await new_document_for_update(session=session, existing_documents=existing_documents, questions_data=questions_data, new_survey=new_survey)
    await new_multiple_choice_for_update(session=session, existing_multiple_choices=existing_multiple_choices, questions_data=questions_data, new_survey=new_survey)
    await new_single_choice_for_update(session=session, existing_single_choices=existing_single_choices, questions_data=questions_data, new_survey=new_survey)

    await session.delete(existing_survey)
    await session.commit()

    return new_survey

@async_session
async def get_survey_by_title(session: AsyncSession, survey_title: str) -> Dict:
    """Filtra o formulário pelo titulo"""
    
    survey_data = await get_one_and_filter_survey(session=session, survey_obj=Survey.title, param=survey_title)
    return survey_data
    
@async_session
async def get_survey_by_theme(session: AsyncSession, survey_theme_id: int) -> Dict:
    """Filtra o formulário pelo tema"""
    
    survey_data = await get_one_and_filter_survey(session=session, survey_obj=Survey.theme_id, param=survey_theme_id)
    return survey_data

@async_session
async def get_survey_by_answered(session: AsyncSession, answered: bool) -> Dict:
    """Filtra o formulário pelo tema"""
    
    if answered: 
        survey_data = await get_one_and_filter_survey(session=session, survey_obj=Survey.answered, param=True)
        return survey_data
    
    survey_data = await get_one_and_filter_survey(session=session, survey_obj=Survey.answered, param=False)
    return survey_data

@async_session
async def remove(session: AsyncSession, survey_id: int) -> Dict[str, str]:
    """Deleta formulários"""

    obj_id = await session.execute(select(Survey).where(Survey.id == survey_id))
    obj_survey = obj_id.scalar_one()
    await session.delete(obj_survey)
    await session.commit()
    return {"message": "Formulário deletado com sucesso"}