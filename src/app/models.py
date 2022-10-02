import datetime
from decimal import Decimal
from pydantic import BaseModel


class BankCard(BaseModel):
    number: str
    balance: Decimal
    expired_at: datetime.datetime
