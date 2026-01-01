from api.v1.apps.questions.models.models import Text, MultipleChoice, SingleChoice, Email, Document, Scale, MultiQuestionMulti, MultiQuestionSingle
from api.v1.apps.survey.models.models import Survey
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import async_session
from loguru import logger
from typing import Dict


@async_session
async def register_survey(session: AsyncSession, survey_id: int, user_id: int, title:str, description:str) -> Dict[str, str]:
    """Salva os dados do formulário"""
    
    new_survey = Survey(id=survey_id,user_id=user_id, title=title, description=description)
    logger.info(f'Criando novo survey: {new_survey}')
    session.add(new_survey)
    await session.commit()
    logger.success(f'Formulário com o título: {new_survey.title} foi salvo com sucesso')
    return {"message": f'Formulário com o título: {new_survey.title} foi salvo com sucesso'}

@async_session
async def register_scale(session: AsyncSession, id:int, survey_id: int, type:str, input_type:str, text:str, scale_min:int, scale_max:int, order:int) -> Dict[str, str]:
    """Salva os dados do formulário"""

    new_survey = Scale(id=id, survey_id=survey_id, type=type, input_type=input_type, text=text, scale_min=scale_min, scale_max=scale_max, order=order)
    logger.info(f'Criando novo survey: {new_survey}')
    session.add(new_survey)
    await session.commit()
    logger.success(f'Formulário com o título: {new_survey.text} foi salvo com sucesso')
    return {"message": f'Formulário com o título: {new_survey.text} foi salvo com sucesso'}

@async_session
async def register_text(session: AsyncSession, id: int, survey_id: int, type: str, input_type: str, text:str, order:int) -> Dict[str, str]:
    """Salva os dados da pergunta text"""
    
    new_survey = Text(id=id, survey_id=survey_id, type=type, input_type=input_type, text=text, order=order)
    logger.info(f'Criando novo survey: {new_survey}')
    session.add(new_survey)
    await session.commit()
    logger.success(f'A pergunta com o texto: {new_survey.text} foi salva com sucesso')
    return {"message": f'A pergunta com o texto: {new_survey.text} foi salva com sucesso'}

@async_session
async def register_multi_choice(session: AsyncSession, id: int, survey_id: int, type: str, input_type: str, text:str, order:int) -> Dict[str, str]:
    """Salva os dados da pergunta multi_choice"""

    new_multi_choice = MultipleChoice(id=id, survey_id=survey_id, type=type, input_type=input_type, text=text, order=order)
    logger.info(f'Criando novo survey: {new_multi_choice}')
    session.add(new_multi_choice)
    await session.commit()
    logger.success(f'Pergunta com o texto: {new_multi_choice.text} foi salva com sucesso')
    return {"message": f'Pergunta com o texto: {new_multi_choice.text} foi salva com sucesso'}
    

@async_session
async def register_single_choice(session: AsyncSession, id: int, survey_id: int, type:str, input_type:str, text:str, order:int) -> Dict[str, str]:
    """Salva os dados da pergunta single_choice"""
    
    new_single_choice = SingleChoice(id=id, survey_id=survey_id, type=type, input_type=input_type, text=text, order=order)
    logger.info(f'Criando novo survey: {new_single_choice}')
    session.add(new_single_choice)
    await session.commit()
    logger.success(f'Pergunta com o texto: {new_single_choice.text} foi salva com sucesso')
    return {"message": f'Pergunta com o texto: {new_single_choice.text} foi salva com sucesso'}


@async_session
async def register_email(session: AsyncSession, id: int, survey_id: int, type: str, input_type: str, text:str, order:int) -> Dict[str, str ]:
    """Salva os dados da pergunta email"""
    
    new_email = Email(id=id, survey_id=survey_id, type=type, input_type=input_type, text=text, order=order)
    logger.info(f'Criando novo survey: {new_email}')
    session.add(new_email)
    await session.commit()
    logger.success(f'Pergunta com o texto: {new_email.text} foi salva com sucesso')
    return {"message": f'Pergunta com o texto: {new_email.text} foi salva com sucesso'}


@async_session
async def register_document(session: AsyncSession, id: int, survey_id: int, type: str, input_type: str, text:str, order:int) -> Dict[str, str]:
    """Salva os dados da pergunta document"""

    new_document = Document(id=id, survey_id=survey_id, type=type, input_type=input_type, text=text, order=order)
    logger.info(f'Criando novo survey: {new_document}')
    session.add(new_document)
    await session.commit()
    logger.success(f'Pergunta com o texto: {new_document.text} foi salva com sucesso')
    return {"message": f'Pergunta com o texto: {new_document.text} foi salva com sucesso'}
    

@async_session
async def register_multi_question_multi(session: AsyncSession, id: int, multi_choice_id: int, text:str) -> Dict[str, str]:
    """Salva os dados de multi_questions da pergunta multiple_choice"""

    new_multi_questions = MultiQuestionMulti(id=id, multi_choice_id=multi_choice_id, text=text)
    logger.info(f'Criando novo survey: {new_multi_questions}')
    session.add(new_multi_questions)
    await session.commit()
    logger.success(f'Pergunta com o texto: {new_multi_questions.text} foi salva com sucesso')
    return {"message": f'Pergunta com o texto: {new_multi_questions.text} foi salva com sucesso'}


@async_session
async def register_multi_question_single(session: AsyncSession, id: int, single_choice_id: int, text:str) -> Dict[str, str]:
    """Salva os dados de multi_questions da pergunta single_choice"""

    new_multi_questions = MultiQuestionSingle(id=id, single_choice_id=single_choice_id, text=text)
    logger.info(f'Criando novo survey: {new_multi_questions}')
    session.add(new_multi_questions)
    await session.commit()
    logger.success(f'Pergunta com o texto: {new_multi_questions.text} foi salva com sucesso')
    return {"message": f'Pergunta com o texto: {new_multi_questions.text} foi salva com sucesso'}

