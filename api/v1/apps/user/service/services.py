from api.v1.apps.user.models.models import Users
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import async_session
from typing import Dict
from loguru import logger


@async_session
async def insert(session: AsyncSession, id: int, username: str, email: str, name: str) -> Dict[str, str]:
    """Função para salvar informações dos clientes"""

    new_user = Users(id=id, username=username, email=email, name=name)
    session.add(new_user)
    await session.commit()
    logger.success("Novo usuário registrado com sucesso")
    return {"message": "Usuário salvo com sucesso"}