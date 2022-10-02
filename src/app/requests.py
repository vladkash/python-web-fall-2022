from decimal import Decimal
from pydantic import BaseModel
from app.models import BankCard


class ConsumptionRequest(BaseModel):
    bank_card: BankCard
    amount: Decimal
