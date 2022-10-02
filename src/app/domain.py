import datetime
import logging
from decimal import Decimal

import grpc
from fastapi import HTTPException

from app.models import BankCard
from generated.service_pb2 import ConsumptionInfo
from generated.service_pb2_grpc import TestServiceStub


def consumption(bank_card: BankCard, amount: Decimal):
    if bank_card.balance < amount:
        raise HTTPException(400, "Not enough money!")

    if amount <= 0:
        raise HTTPException(400, "Consumption amount is invalid!")

    bank_card.balance -= amount

    return bank_card


def send_receipt(bank_card: BankCard, amount: Decimal):
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)

        confirmation = client.CreateReceipt(ConsumptionInfo(
            card_number=bank_card.number,
            amount=amount * 100,
        ))

        print(confirmation.message)
