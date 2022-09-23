import datetime
from decimal import Decimal

from exceptions import LoggingException
from models import BankCard


def log_consumption(bank_card: BankCard, amount: Decimal):
    try:
        with open(f"logs/{datetime.datetime.now().strftime('%Y-%m-%d')}.log", "a") as log_file:
            log_file.write(
                f"Consumption from card {bank_card.number}, amount {amount}, now balance is {bank_card.balance}\n")
    except Exception:
        raise LoggingException("Logging error")
