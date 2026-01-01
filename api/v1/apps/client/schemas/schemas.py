from pydantic import BaseModel

class ClientSchema(BaseModel):
    email: str