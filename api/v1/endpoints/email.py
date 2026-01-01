from fastapi import APIRouter, BackgroundTasks
from configs.config import MailBody
from helpers.send_mail import send_email

router = APIRouter()


@router.post("/send-mail")
async def schedule_email(req: MailBody, tasks: BackgroundTasks):
    data = req.dict()
    tasks.add_task(send_email, data)
    return {"status": 200, "message": "email enviado com sucesso"}