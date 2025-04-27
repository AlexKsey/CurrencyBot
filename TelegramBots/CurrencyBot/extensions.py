import requests
import json


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float) -> float:
        url = f"https://api.exchangerate-api.com/v4/latest/{base.upper()}"
        r = requests.get(url)
        data = json.loads(r.text)

        if quote.upper() not in data['rates']:
            raise APIException(f"Валюта {quote} не найдена")

        return round(data['rates'][quote.upper()] * amount, 2)