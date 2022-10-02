import datetime
from decimal import Decimal

from fastapi import HTTPException
from parameterized import parameterized
import unittest
from app.domain import consumption
from app.models import BankCard


class ConsumptionTest(unittest.TestCase):
    @parameterized.expand([
        [BankCard.construct(number="5272690236059133", balance=100,
                            expired_at=datetime.datetime.today() + datetime.timedelta(days=1)), 200],
        [BankCard.construct(number="5272690236059133", balance=100,
                            expired_at=datetime.datetime.today() + datetime.timedelta(days=1)), -200],
    ])
    def test_wrong_cases(self, bank_card: BankCard, amount: Decimal):
        with self.assertRaises(HTTPException):
            consumption(bank_card, amount)

    def test_correct_consumption(self):
        amount = Decimal(100)
        balance = 200
        bank_card = BankCard.construct(number="5272690236059133", balance=balance,
                                       expired_at=datetime.datetime.today() + datetime.timedelta(days=1))
        consumption(bank_card, amount)
        self.assertEqual(balance - amount, bank_card.balance)
