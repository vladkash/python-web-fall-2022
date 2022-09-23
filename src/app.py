from decimal import getcontext

from fastapi import FastAPI, Request

from exceptions import APIException
from logs import log_consumption
from validation import check_card
from domain import consumption

from requests import ConsumptionRequest

app = FastAPI()
# работаем с числами не больше 2 знаков после запятой
getcontext().prec = 2


@app.post("/consumption")
async def store_item(request: ConsumptionRequest):
    check_card(request.bank_card)
    consumption(request.bank_card, request.amount)
    log_consumption(request.bank_card, request.amount)
    return {
        "success": True,
        "message": "Consumption is successfull"
    }


@app.exception_handler(APIException)
async def api_exception_handler(request: Request, e: APIException):
    return {
        "success": True,
        "message": e.message
    }
