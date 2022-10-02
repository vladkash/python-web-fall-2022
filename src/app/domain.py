import datetime
import logging
from decimal import Decimal

from fastapi import HTTPException

from app.models import BankCard


def consumption(bank_card: BankCard, amount: Decimal):
    if bank_card.balance < amount:
        raise HTTPException(400, "Not enough money!")

    if amount <= 0:
        raise HTTPException(400, "Consumption amount is invalid!")

    bank_card.balance -= amount

    return bank_card


def send_receipt(bank_card: BankCard, amount: Decimal):
    logging.basicConfig(filename=f"logs/{datetime.datetime.now().strftime('%Y-%m-%d')}.log", encoding='utf-8',
                        level=logging.DEBUG)
    logging.getLogger(__name__).info(
        f"Consumption from card {bank_card.number}, amount {amount}, now balance is {bank_card.balance}")
