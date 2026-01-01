from api.v1.apps.theme.service.services import insert, get_all, get_one, update, remove
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from api.v1.apps.theme.schemas.schemas import ThemeSchema
from helpers.auth_utils import JWTBearer, format_jwt
from sqlalchemy.ext.asyncio import AsyncSession
from configs.config import SUPER_ADMIN, ADMIN
from sqlalchemy.orm.exc import NoResultFound
from db.session import get_async_session
from loguru import logger

router = APIRouter()

@router.post('/create-theme/')
async def create_theme(theme: ThemeSchema, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para criação de temas"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:

            return await insert(description=theme.description)
    
    except IntegrityError as e:
        logger.error(f"Erro de integridade ao salvar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Violação de integridade ao salvar tema")
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao salvar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao salvar tema")
    except Exception as e:
        logger.error(f"Erro inesperado ao salvar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao salvar tema")
    

@router.get('/get-theme/')
async def get_theme(dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para listagem dos Temas"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_all(ThemeSchema)
    
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar temas: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar temas")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar temas: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar temas")
    

@router.get('/get-one-theme/{theme_id}/')
async def get_one_theme(theme_id: int, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para resgatar apenas um tema"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await get_one(theme_id=theme_id)
    
    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Tema não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao resgatar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao resgatar tema")
    except Exception as e:
        logger.error(f"Erro inesperado ao resgatar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao resgatar tema")
    

@router.put('/update-theme/{theme_id}/')
async def update_theme(theme_id: int, theme: ThemeSchema, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para atualizar temas"""

    try:
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await update(theme_id=theme_id, description=theme.description)
    
    except IntegrityError as e:
        logger.error(f"Erro de integridade ao atualizar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Violação de integridade ao atualizar tema")
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao atualizar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao atualizar tema")
    except Exception as e:
        logger.error(f"Erro inesperado ao atualizar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar tema")
    

@router.delete('/delete-theme/{theme_id}/')
async def delete_theme(theme_id: int, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(get_async_session)):
    """Endpoint para deletar tema"""

    try: 
        decoded_payload = format_jwt(dependencies)
        usuario = decoded_payload.get('role')
        
        if usuario == SUPER_ADMIN or usuario == ADMIN:
            return await remove(theme_id=theme_id)
    
    except NoResultFound:
        logger.error(f"Não existe registro no banco de dados com esse id: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Tema não encontrado'}) 
    except SQLAlchemyError as e:
        logger.error(f"Erro de banco de dados ao deletar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro de banco de dados ao deletar tema")
    except Exception as e:
        logger.error(f"Erro inesperado ao deletar tema: {e}")
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar tema")