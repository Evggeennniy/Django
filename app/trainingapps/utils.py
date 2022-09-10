# low level code this

from decimal import Decimal
import requests


def to_decimal(value: str, precision: int = 2) -> Decimal:
    """
    Function for retype to Decimal
    """

    return round(Decimal(value), precision)


def get_json_from_url(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def get_txt_from_url(url: str) -> str:
    response = requests.get(url)
    txt = response.text

    return txt


def is_number(s: str) -> bool:
    """
    Returns True is string is a int or float.
    """
    if s.isdigit():
        return True
    elif s.replace('.', '').isdigit():
        return True
    else:
        return False


def eazyhandler(
    data: list,
    cutleft: int = None,
    cutright: int = None,
    onlynumber: bool = False,
    max_len: int = None,
) -> list:

    """
    Lightweight handler with cropping and sorting options.
    """
    ready_data = []

    for element in data:
        element = element.text

        if not onlynumber:
            ready_data += [element[cutleft:cutright]]
        if onlynumber:
            element = element[cutleft:cutright]
            if is_number(element):
                ready_data += [element]

    ready_data = ready_data[:max_len]

    return ready_data


def picker_datas_onetotwo(firstdata: list, nextdata: list):
    """
    The assembler makes a match between two data.
    """
    ready_data = []
    for name in firstdata:
        data = {
            'ccy': name,

            'buy': nextdata.pop(0),
            'sale': nextdata.pop(0),
        }
        ready_data += [data]

    return ready_data


def picker_datas_onetofour(firstdata: list, nextdata: list):
    """
    The assembler makes a match between two data.
    """
    ready_data = []
    for name in firstdata:
        data = {
            'ccy': name,

            'buy': nextdata.pop(0),
            'sale': nextdata.pop(0),
            'args0': nextdata.pop(0),
            'args1': nextdata.pop(0),
        }
        ready_data += [data]

    return ready_data
