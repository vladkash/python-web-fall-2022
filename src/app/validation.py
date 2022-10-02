import datetime

from fastapi import HTTPException

from app.models import BankCard


def check_card(card: BankCard):
    if not card_number_is_valid(card.number):
        raise HTTPException(400, "Card number is not valid")
    if card_expired(card.expired_at):
        raise HTTPException(400, "Card number is expired")


def card_number_is_valid(card_number: str):
    """
    Проверка корректности номера карты
    использует алгоритм Луна
    :param card_number: номер карты
    :return: корректен ли переданный номер карты
    """
    n_digits = len(card_number)

    if n_digits != 16:
        return False

    n_sum = 0

    is_second = False

    for i in range(n_digits - 1, -1, -1):
        d = ord(card_number[i]) - ord('0')
        if is_second:
            d = d * 2
        n_sum += d // 10
        n_sum += d % 10
        is_second = not is_second

    if n_sum % 10 == 0:
        return True
    else:
        return False


def card_expired(expired_date: datetime.datetime) -> bool:
    """
    Проверка даты истечения срока действия карты
    :param expired_date: до какой даты действует карта
    :return: действует ли карта сейчас
    """
    return expired_date < datetime.datetime.now()
