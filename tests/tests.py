import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status
from main import app  # substitua pelo caminho correto para o app FastAPI
from db.session import get_async_session, AsyncSessionLocal  # substitua pelo caminho correto para seu banco de dados
from api.v1.apps.theme.models.models import Theme  # substitua pelo caminho correto para seu modelo Theme
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError


# Sobrescreva a dependência de sessão para usar um banco de dados de teste
@pytest.fixture
async def async_session_override():
    async with AsyncSessionLocal() as session:
        yield session

app.dependency_overrides[get_async_session] = async_session_override

@pytest.fixture
async def async_session_override():
    async with AsyncSessionLocal() as session:
        yield session

app.dependency_overrides[get_async_session] = async_session_override

@pytest.mark.asyncio
async def test_create_theme_success(async_session_override):
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as client:
        payload = {"description": "Test Theme"}
        response = await client.post("/theme/create-theme/", json=payload)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "id" in data  # Verifica se o id foi retornado

        # Verifica se o tema foi realmente salvo no banco de dados
        result = await async_session_override.execute(
            select(Theme).where(Theme.description == "Test Theme")
        )
        theme = result.scalars().first()
        assert theme is not None
        assert theme.description == "Test Theme"

@pytest.mark.asyncio
async def test_create_theme_integrity_error(async_session_override):
    async with async_session_override as session:
        new_theme = Theme(description="Duplicate Theme")
        session.add(new_theme)
        await session.commit()

    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {"description": "Duplicate Theme"}
        response = await client.post("/create-theme/", json=payload)
        
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json()["detail"] == "Violação de integridade ao salvar tema"

@pytest.mark.asyncio
async def test_create_theme_database_error(monkeypatch):
    async def mock_insert(*args, **kwargs):
        raise SQLAlchemyError("Database Error")
    
    monkeypatch.setattr("api.v1.endpoints.theme.create_theme.insert", mock_insert)  # Substitua pelo caminho real do seu módulo
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {"description": "Theme Causing Error"}
        response = await client.post("/create-theme/", json=payload)
        
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.json()["detail"] == "Erro de banco de dados ao salvar tema"

@pytest.mark.asyncio
async def test_create_theme_unexpected_error(monkeypatch):
    async def mock_insert(*args, **kwargs):
        raise Exception("Unexpected Error")
    
    monkeypatch.setattr("api.v1.endpoints.theme.create_theme.create_theme.insert", mock_insert)  # Substitua pelo caminho real do seu módulo
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {"description": "Theme Causing Unexpected Error"}
        response = await client.post("/create-theme/", json=payload)
        
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.json()["detail"] == "Erro ao salvar tema"