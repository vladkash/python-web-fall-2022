from decimal import Decimal

from models import BankCard

from exceptions import ConsumptionException


def consumption(bank_card: BankCard, amount: Decimal):
    if bank_card.balance < amount:
        raise ConsumptionException("Not enough money!")

    if amount <= 0:
        raise ConsumptionException("Consumption amount is invalid!")

    bank_card.balance -= amount

    return bank_card
