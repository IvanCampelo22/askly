from fastapi.routing import APIRouter
from api.v1.endpoints import clients
from api.v1.endpoints import theme
from api.v1.endpoints import nps
from api.v1.endpoints import auth
from api.v1.endpoints import email

api_router = APIRouter()

api_router.include_router(nps.router, prefix='/nps', tags=['nps'])
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(theme.router, prefix='/theme', tags=['theme'])
api_router.include_router(clients.router, prefix='/client', tags=['client'])
api_router.include_router(email.router, prefix='/email', tags=['email'])


