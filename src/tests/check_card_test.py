import datetime
import unittest

from fastapi import HTTPException
from parameterized import parameterized
from app.validation import check_card
from app.models import BankCard


class CheckCardTest(unittest.TestCase):
    def test_checking_correct_card(self):
        check_card(BankCard.construct(number="5272690236059133", balance=100,
                                      expired_at=datetime.datetime.today() + datetime.timedelta(days=1)))

    @parameterized.expand([
        [BankCard.construct(number="", balance=100, expired_at=datetime.datetime.today() + datetime.timedelta(days=1))],
        [BankCard.construct(number="5272690236059133", balance=100,
                            expired_at=datetime.datetime.today() - datetime.timedelta(days=1))],
    ])
    def test_checking_incorrect_card(self, bank_card):
        with self.assertRaises(HTTPException):
            check_card(bank_card)
