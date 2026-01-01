from api.v1.apps.questions.models.models import Text, Scale, Email, Document, MultipleChoice, MultiQuestionMulti, SingleChoice, MultiQuestionSingle
from sqlalchemy.ext.asyncio import AsyncSession
from helpers.common import validate_and_update
from sqlalchemy.orm import selectinload
from db.session import async_session
from sqlalchemy.future import select
from typing import Dict

@async_session
async def update_text(session: AsyncSession, text_id: int, **kwargs) -> Dict:
    """Atualiza pergunta do tipo texto"""

    text_question = await session.execute(select(Text).where(Text.id == text_id))
    existing_text = text_question.scalars().first()

    await validate_and_update(existing_text, **kwargs)

    await session.commit()
    return existing_text

@async_session
async def update_scale(session: AsyncSession, scale_id: int, **kwargs) -> Dict:
    """Atualiza pergunta do tipo scale"""

    scale_question = await session.execute(select(Scale).where(Scale.id == scale_id))
    existing_scale = scale_question.scalars().first()

    await validate_and_update(existing_scale, **kwargs)

    await session.commit()
    return existing_scale

@async_session
async def update_multiple_choice(session: AsyncSession, multi_id: int, question_multi, **kwargs) -> Dict:
    """Atualiza pergunta do tipo multiplas escolhas"""

    multi_question = await session.execute(select(MultipleChoice).where(MultipleChoice.id == multi_id).options(selectinload(MultiQuestionMulti)).where(MultiQuestionMulti.id == question_multi))
    existing_multi = multi_question.scalars().first()

    await validate_and_update(existing_multi, **kwargs)

    await session.commit()
    return existing_multi

@async_session
async def update_single_choice(session: AsyncSession, single_id: int, **kwargs) -> Dict:
    """Atualiza pergunta do tipo multiplas escolhas"""

    multi_question = await session.execute(select(SingleChoice).where(SingleChoice.id == single_id))
    existing_multi = multi_question.scalars().first()

    await validate_and_update(existing_multi, **kwargs)

    await session.commit()
    return existing_multi

@async_session
async def update_email(session: AsyncSession, email_id: int, **kwargs) -> Dict:
    """Atualiza pergunta do tipo email"""

    email_question = await session.execute(select(Email).where(Email.id == email_id))
    existing_email = email_question.scalars().first()

    await validate_and_update(existing_email, **kwargs)

    await session.commit()
    return existing_email

@async_session
async def update_document(session: AsyncSession, document_id: int, **kwargs) -> Dict:
    """Atualiza pergunta do tipo documentos"""

    document_question = await session.execute(select(Document).where(Document.id == document_id))
    existing_document = document_question.scalars().first()

    await validate_and_update(existing_document, **kwargs)

    await session.commit()
    return existing_document

@async_session
async def update_multi_question(session: AsyncSession, question_multi_id: int, **kwargs) -> Dict:
    """Atualiza pergunta do tipo multi questions for multiple choices"""

    multi_question = await session.execute(select(MultiQuestionMulti).where(MultiQuestionMulti.id == question_multi_id))
    existing_multi_question = multi_question.scalars().first()

    await validate_and_update(existing_multi_question, **kwargs)

    await session.commit()
    return existing_multi_question


@async_session
async def update_single_question(session: AsyncSession, question_single_id: int, **kwargs) -> Dict:
    """Atualiza pergunta do tipo questions for single choices"""

    single_question = await session.execute(select(MultiQuestionSingle).where(MultiQuestionSingle.id == question_single_id))
    existing_single_question = single_question.scalars().first()

    await validate_and_update(existing_single_question, **kwargs)

    await session.commit()
    return existing_single_question