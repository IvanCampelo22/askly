from api.v1.apps.client.service.services import insert, get_all, get_one, update, remove, get_client_by_email
from fastapi import APIRouter, HTTPException, status, Depends
from api.v1.apps.client.schemas.schemas import ClientSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from configs.config import SUPER_ADMIN, ADMIN
from helpers.auth_utils import JWTBearer, format_jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound
from db.session import get_async_session
from loguru import logger

router = APIRouter()

@router.post('/create-client/')
async def create_client(client: ClientSchema, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para criação de clientes"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await insert(email=client.email)
    
    except IntegrityError as e:
        logger.error(f"Erro de integridade ao salvar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Violação de integridade ao salvar cliente")
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao salvar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao salvar cliente")
    except Exception as e:
        logger.error(f"Erro inesperado ao salvar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao salvar cliente")
    

@router.get('/get-client/')
async def get_client(dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para listagem dos clientes"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_all(ClientSchema)
    
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar clientes: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar clientes")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar clientes: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar clientes")
    

@router.get('/get-one-client/{client_id}/')
async def get_one_client(client_id: int, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para resgatar apenas um cliente"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_one(client_id=client_id)
    
    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Cliente não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar cliente")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar cliente")
    

@router.get('/filter-client-by-email/')
async def get_one_client(client_email: str, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para resgatar cliente por email"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_client_by_email(client_email=client_email)
    
    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Cliente não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar cliente")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar cliente")
    

@router.put('/update-client/{client_id}/')
async def update_client(client_id: int, client: ClientSchema, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para atualizar clientes"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await update(client_id=client_id, email=client.email)
    
    except IntegrityError as e:
        logger.error(f"Erro de integridade ao atualizar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Violação de integridade ao atualizar cliente")
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao atualizar client: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao atualizar cliente")
    except Exception as e:
        logger.error(f"Erro inesperado ao atualizar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar cliente")
    

@router.delete('/delete-client/{client_id}/')
async def delete_client(client_id: int, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para deletar cliente"""

    try: 
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await remove(client_id=client_id)
    
    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Cliente não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao deletar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao deletar cliente")
    except Exception as e:
        logger.error(f"Erro inesperado ao deletar cliente: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar cliente")