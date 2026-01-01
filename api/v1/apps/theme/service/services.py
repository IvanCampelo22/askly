from api.v1.apps.theme.schemas.schemas import ThemeSchema
from api.v1.apps.theme.models.models import Theme
from sqlalchemy.ext.asyncio import AsyncSession
from helpers.common import validate_and_update
from db.session import async_session
from sqlalchemy.future import select
from typing import List, Dict
from loguru import logger


@async_session
async def insert(session: AsyncSession, description: str) -> Dict[str, str]:
    """Função para salvar informações dos Temas"""

    new_theme = Theme(description=description)
    session.add(new_theme)
    await session.commit()
    logger.success("Novo tema registrado com sucesso")
    return {"message": "Tema salvo com sucesso"}

@async_session
async def get_all(session: AsyncSession, theme_schema) -> List[ThemeSchema]:
    """Função para listar todos os temas"""

    query = select(Theme)
    result = await session.execute(query)
    list: List[theme_schema] = result.scalars().all()
    return list
    
@async_session
async def get_one(session: AsyncSession, theme_id: int) -> Dict:
    """Pega um tema pelo identificador"""

    obj = await session.execute(select(Theme).where(Theme.id == theme_id))
    obj_theme = obj.scalar_one()
    return obj_theme

@async_session
async def update(session: AsyncSession, theme_id: int, **kwargs) -> Dict:
    """Atualiza temas"""

    theme = await session.execute(select(Theme).where(Theme.id == theme_id))
    existing_theme = theme.scalars().first()

    await validate_and_update(existing_theme, **kwargs)

    await session.commit()
    return existing_theme

@async_session
async def remove(session: AsyncSession, theme_id: int) -> Dict[str, str]:
    """Deleta temas"""

    obj_id = await session.execute(select(Theme).where(Theme.id == theme_id))
    obj_theme = obj_id.scalar_one()
    await session.delete(obj_theme)
    await session.commit()
    return {"message": "Tema deletado com sucesso"}
    
   