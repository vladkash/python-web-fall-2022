import datetime
import unittest
from parameterized import parameterized
from decimal import Decimal

from app.domain import send_receipt
from app.models import BankCard


class SendingReceiptTest(unittest.TestCase):
    @parameterized.expand([
        [BankCard.construct(number="5272690236059133", balance=100,
                            expired_at=datetime.datetime.today() + datetime.timedelta(days=1)), 50],
        [BankCard.construct(number="5272690236059133", balance=100,
                            expired_at=datetime.datetime.today() + datetime.timedelta(days=1)), 80],
        [BankCard.construct(number="5272690236059133", balance=100,
                            expired_at=datetime.datetime.today() + datetime.timedelta(days=1)), 90]
    ])
    def test_sending(self, bank_card: BankCard, amount: Decimal):
        send_receipt(bank_card, amount)
