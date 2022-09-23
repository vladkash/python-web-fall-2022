from decimal import Decimal
from pydantic import BaseModel
from models import BankCard


class ConsumptionRequest(BaseModel):
    bank_card: BankCard
    amount: Decimal
