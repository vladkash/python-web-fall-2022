from decimal import getcontext

from fastapi import FastAPI, Request

from app.validation import check_card
from app.domain import consumption, send_receipt

from app.requests import ConsumptionRequest

app = FastAPI()
# работаем с числами не больше 2 знаков после запятой
getcontext().prec = 2


@app.post("/consumption")
async def consumption_from_card(request: ConsumptionRequest):
    """
    Метод списания с карты денег
    Проверяет корректность карты, списывает деньги
    И отправляет чек
    :param request: Запрос, содержащий информацию о карте и сумме списания
    :return:
    """
    check_card(request.bank_card)
    consumption(request.bank_card, request.amount)
    send_receipt(request.bank_card, request.amount)
    return {
        "success": True,
        "message": "Consumption is successfull"
    }
