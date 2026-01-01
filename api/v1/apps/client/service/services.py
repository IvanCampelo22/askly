from api.v1.apps.client.schemas.schemas import ClientSchema
from api.v1.apps.client.models.models import Client
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import async_session
from sqlalchemy.future import select
from typing import List, Dict
from loguru import logger


@async_session
async def insert(session: AsyncSession, email: str) -> Dict[str, str]:
    """Função para salvar informações dos clientes"""

    new_client = Client(email=email)
    session.add(new_client)
    await session.commit()
    logger.success("Novo cliente registrado com sucesso")
    return {"message": "Cliente salvo com sucesso"}


@async_session
async def get_all(session: AsyncSession, client_schema) -> List[ClientSchema]:
    """Função para listar todos os clientes"""

    query = select(Client)
    result = await session.execute(query)
    list: List[client_schema] = result.scalars().all()
    return list
    

@async_session
async def get_one(session: AsyncSession, client_id: int) -> Dict:
    """Pega um cliente pelo identificador"""

    obj = await session.execute(select(Client).where(Client.id == client_id))
    obj_client = obj.scalar_one()
    return obj_client

@async_session
async def get_client_by_email(session: AsyncSession, client_email: str) -> Dict:
    """Pega um cliente pelo email"""

    obj = await session.execute(select(Client).where(Client.email == client_email))
    obj_client = obj.scalar_one()
    return obj_client
    

@async_session
async def update(session: AsyncSession, client_id: int, email: str) -> Dict:
    """Atualiza clientes"""

    client = await session.execute(select(Client).where(Client.id == client_id))
    existing_client = client.scalars().first()

    if email is not None:
        existing_client.email  = email
    else: 
        existing_client.email = existing_client.email

    existing_client.email = email

    await session.commit()
    return existing_client
    

@async_session
async def remove(session: AsyncSession, client_id: int) -> Dict[str, str]:
    """Deleta clientes"""

    obj_id = await session.execute(select(Client).where(Client.id == client_id))
    obj_client = obj_id.scalar_one()
    await session.delete(obj_client)
    await session.commit()
    return {"message": "Cliente deletado com sucesso"}
    
   