class APIException(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidCardException(APIException):
    pass


class ConsumptionException(APIException):
    pass


class LoggingException(APIException):
    pass
