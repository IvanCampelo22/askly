import os 
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List

load_dotenv()

MAIL_USERNAME=os.environ.get("MAIL_HOST")
MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
MAIL_FROM=os.environ.get("MAIL_FROM")
MAIL_PORT=os.environ.get("MAIL_PORT")
MAIL_SERVER=os.environ.get("MAIL_SERVER")
MAIL_FROM_NAME=os.environ.get("MAIL_FROM_NAME")
USER=os.environ.get("USER_SURVEY")
PASSWORD=os.environ.get("PASSWORD_SURVEY")
HOST=os.environ.get("HOST_SURVEY")
NAME=os.environ.get("NAME_SURVEY")
JWT_SECRET_KEY=os.environ.get("SECRET")
ALGORITHM=os.environ.get("ALGORITHM")
SUPER_ADMIN=os.environ.get("SUPER_ADMIN")
ADMIN=os.environ.get("ADMIN")
VIEWER=os.environ.get("VIEWER")

class MailBody(BaseModel):
    to: List[str]
    subject: str
    body: str