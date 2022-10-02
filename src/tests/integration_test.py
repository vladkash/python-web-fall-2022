import unittest
import datetime
from decimal import Decimal

from fastapi.testclient import TestClient
from parameterized import parameterized
from app.main import app
from app.models import BankCard


class IntegrationTest(unittest.TestCase):
    api = TestClient(app, raise_server_exceptions=True)

    @parameterized.expand([
        [BankCard.construct(number="5272690236059133", balance=100, expired_at=datetime.datetime.today() + datetime.timedelta(days=1)),
         50],
    ])
    def test_correct_request(self, bank_card: BankCard, amount: Decimal):
        response = self.api.request('post', '/consumption', json={'bank_card': {'number': bank_card.number, 'balance': bank_card.balance, 'expired_at': bank_card.expired_at.isoformat()}, 'amount': amount})
        self.assertTrue(response.json()['success'])

    @parameterized.expand([
        [BankCard.construct(number="", balance=100, expired_at=datetime.datetime.today() + datetime.timedelta(days=1)), 50],
        [BankCard.construct(number="5272690236059133", balance=100, expired_at=datetime.datetime.today() - datetime.timedelta(days=1)), 50],
    ])
    def test_incorrect_requests(self, bank_card: BankCard, amount: Decimal):
        response = self.api.request('post', '/consumption', json={'bank_card': {'number': bank_card.number, 'balance': bank_card.balance, 'expired_at': bank_card.expired_at.isoformat()}, 'amount': amount})
        self.assertEqual(response.status_code, 400)
