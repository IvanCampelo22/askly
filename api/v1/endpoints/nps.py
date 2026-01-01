from helpers.register_survey_infos import register_survey, register_text, register_single_choice, register_document, register_email, register_multi_choice, register_scale, register_multi_question_multi, register_multi_question_single
from api.v1.apps.questions.service.services import update_text, update_scale, update_email, update_document, update_single_choice, update_multiple_choice, update_multi_question, update_single_question
from api.v1.apps.questions.schemas.schemas import TextSchema, ScaleSchema, MultipleChoice, SingleChoice, EmailSchema, DocumentSchema, MultiQuestionSingleSchema, MultiQuestionMultipleSchema
from api.v1.apps.survey.service.services import get_one, remove, update, get_survey_by_title, get_survey_by_theme, get_survey_by_answered
from api.v1.apps.user.service.services import insert as insert_user
from fastapi import APIRouter, HTTPException, status, Depends
from api.v1.apps.survey.schemas.schemas import SurveySchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from helpers.auth_utils import JWTBearer, format_jwt
from sqlalchemy.ext.asyncio import AsyncSession
from configs.config import SUPER_ADMIN, ADMIN
from sqlalchemy.orm.exc import NoResultFound
from db.session import get_async_session
from fastapi import APIRouter
from typing import Dict, Any
from loguru import logger

router = APIRouter()

@router.post("/get-form/")
async def survey(json: dict, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)) -> Dict[str, str]:
    """Recebe o json que vem do front-end, trata, e salva no banco de dados"""
    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        user_id = decoded_payload.get('user_id')
        username = decoded_payload.get('username')
        name = decoded_payload.get('name')
        email = decoded_payload.get('email')

        await insert_user(id=user_id, username=username, name=name, email=email)

        if usuario == SUPER_ADMIN or usuario == ADMIN:
            survey_id = json["survey"]["id"]
            title = json["survey"]["title"]
            description = json["survey"]["description"]

            await register_survey(survey_id=survey_id, user_id=user_id, title=title, description=description)

            questions = json["survey"]["questions"]

            for index, question in enumerate(questions, start=1):
                type = question["type"]

                if type == "nps":
                    await register_scale(id=question["id"], survey_id=survey_id, type=question["type"], input_type=question["input_type"], text=question["text"], scale_min=question["options"]["scale_min"], scale_max=question["options"]["scale_max"], order=index)

                if type == "text":
                    await register_text(id=question["id"], survey_id=survey_id, type=question["type"], input_type=question["input_type"], text=question["text"], order=index)

                elif type == "multiple_choice":
                    await register_multi_choice(id=question["id"], survey_id=survey_id, type=question["type"], input_type=question["input_type"], text=question["text"], order=index)
                    id_question_multi = question["id"]
                    for op in question["options"]:
                        await register_multi_question_multi(id=op["id"], multi_choice_id=id_question_multi, text=op["text"])

                elif type == "single_choice":
                    await register_single_choice(id=question["id"], survey_id=survey_id, type=question["type"], input_type=question["input_type"], text=question["text"], order=index)
                    id_question_single = question["id"]
                    for op in question["options"]:
                        await register_multi_question_single(id=op["id"], single_choice_id=id_question_single, text=op["text"])

                elif type == "email":
                    await register_email(id=question["id"], survey_id=survey_id, type=question["type"], input_type=question["input_type"], text=question["text"], order=index)

                elif type == "document":
                    await register_document(id=question["id"], survey_id=survey_id, type=question["type"], input_type=question["input_type"], text=question["text"], order=index)

            return {"message": "Formulário salvo com sucesso"}
    
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao salvar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao salvar formulário")
    except Exception as e:
        logger.error(f"Erro inesperado ao salvar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao salvar formulário")


@router.get('/get-one-survey/{survey_id}/')
async def get_one_survey(survey_id: int, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para resgatar apenas um formulário"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_one(survey_id=survey_id)
    
    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Formulário não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar frmulário")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar formulário")


@router.get('/filter-survey-by-title/')
async def filter_survey_by_title(survey_title: str, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)) -> Dict:
    """Endpoint para filtrar formulários pelo titulo """

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_survey_by_title(survey_title=survey_title)
    
    except NoResultFound:
        logger.error(f"Não existe formulário no banco de dados com esse título")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Formulário não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar frmulário")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar formulário")
    

@router.get('/filter-survey-by-theme/')
async def filter_survey_by_theme(survey_theme_id: int, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)) -> Dict:
    """Endpoint para filtrar formulários pelo titulo """

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_survey_by_theme(survey_theme_id=survey_theme_id)
    
    except NoResultFound:
        logger.error(f"Não existe formulário no banco de dados com esse tema")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Formulário não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar frmulário")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar formulário")
    

@router.get('/filter-survey-by-answered/')
async def filter_survey_by_answered(answered: bool = False, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)) -> Dict:
    """Endpoint para filtrar formulários pelo titulo """

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_survey_by_answered(answered=answered)
    
    except NoResultFound:
        logger.error(f"Não existe formulário no banco de dados com esse tema")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Formulário não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar frmulário")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar formulário")


@router.put('/update-survey/{survey_id}/')
async def update_survey(survey_id: int, survey: SurveySchema, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)) -> Any:
    """Endpoint para atualizar formulários"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            survey_data = {
                "title": survey.title,
                "description": survey.description
            }

            questions_data = []

            for option in survey.options:
                option_data = {
                    "type": option.__class__.__name__,
                    "id": option.id
                }
                if isinstance(option, ScaleSchema):
                    option_data.update({
                        "type": option.type,
                        "input_type": option.input_type,
                        "text": option.text,
                        "scale_min": option.scale_min,
                        "scale_max": option.scale_max
                    })
                elif isinstance(option, TextSchema):
                    option_data.update({
                        "type": option.type,
                        "input_type": option.input_type,
                        "text": option.text
                    })
                elif isinstance(option, MultipleChoice):
                    option_data.update({
                        "type": option.type,
                        "input_type": option.input_type,
                        "text": option.text,
                        "options": option.options
                    })
                elif isinstance(option, SingleChoice):
                    option_data.update({
                        "type": option.type,
                        "input_type": option.input_type,
                        "text": option.text,
                        "options": option.options
                    })
                elif isinstance(option, EmailSchema):
                    option_data.update({
                        "type": option.type,
                        "input_type": option.input_type,
                        "text": option.text,
                    })
                elif isinstance(option, DocumentSchema):
                    option_data.update({
                        "type": option.type,
                        "input_type": option.input_type,
                        "text": option.text,
                    })

                questions_data.append(option_data)
            updated_survey = await update(survey_id=survey_id, questions_data=questions_data, **survey_data)
            return updated_survey

    except IntegrityError as e:
        logger.error(f"Erro de integridade ao atualizar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Violação de integridade ao atualizar formulário")
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao atualizar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao atualizar formulário")
    except Exception as e:
        logger.error(f"Erro inesperado ao atualizar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar formulário")


@router.delete('/delete-survey/{survey_id}/')
async def delete_survey(client_id: int, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)) -> Dict[str, str]:
    """Endpoint para deletar formulário"""

    try: 
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await remove(client_id=client_id)
    
    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Formulário não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao deletar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao deletar formulário")
    except Exception as e:
        logger.error(f"Erro inesperado ao deletar formulário: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar formulário")


@router.put('/update-questions/{question_type}/')
async def update_questions(question_type: str, text: TextSchema, scale: ScaleSchema, 
                        email: EmailSchema, document: DocumentSchema, multi: MultipleChoice, 
                        single: SingleChoice, question_single: MultiQuestionSingleSchema,
                        question_multi: MultiQuestionMultipleSchema, 
                        question_id: int,
                        dependencies=Depends(JWTBearer()),
                        session: AsyncSession = Depends(get_async_session)) -> Dict:
    """Endpoint para atualizar perguntas individualmente"""
    
    try: 
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            if question_type == "Text":
                text_data = {
                    "type": text.type,
                    "input_type": text.input_type,
                    "text": text.text
                }
                text_question = await update_text(question_id, **text_data)
                return text_question

            if question_type == "Scale": 
                scale_data = {
                    "type": scale.type,
                    "input_type": scale.input_type,
                    "text": scale.text,
                    "scale_min": scale.scale_min,
                    "scale_max": scale.scale_max,
                }
                scale_question = await update_scale(question_id, **scale_data)
                return scale_question

            if question_type == "Email": 
                email_data = {
                    "type": email.type,
                    "input_type": email.input_type,
                    "text": email.text
                }
                email_question = await update_email(question_id, **email_data)
                return email_question

            if question_type == "Document": 
                document_data = {
                    "type": document.type,
                    "input_type": document.input_type,
                    "text": document.text
                }
                doc_question = await update_document(question_id, **document_data)
                return doc_question

            if question_type == "Single Choice": 
                single_data = {
                    "type": single.type,
                    "input_type": single.input_type,
                    "text": single.text,
                }
                single_choice = await update_single_choice(question_id, **single_data)
                return single_choice

            if question_type == "Multiple Choice": 
                multiple_data = {
                    "type": single.type,
                    "input_type": single.input_type,
                    "text": single.text,
                }
                multiple_choice = await update_multiple_choice(question_id, **multiple_data)
                return multiple_choice

            if question_type == "Multi Question for Multiple Choices": 
                multi_question_data = {
                    "text": question_single.text,
                }

                update_questions_for_multiple = await update_multi_question(question_id, **multi_question_data)
                return update_questions_for_multiple

            if question_type == "Multi Questions for Single Choices": 
                single_question_data = {
                    "text": question_multi.text,
                }

                update_questions_for_single = await update_single_question(question_id, **single_question_data)
                return update_questions_for_single

    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Pergunta não encontrada'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao editar pergunta: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao editar pergunta")
    except Exception as e:
        logger.error(f"Erro inesperado ao editar pergunta: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao editar pergunta")

