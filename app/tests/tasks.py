from unittest.mock import MagicMock
from trainingapps import tasks
from trainingapps.models import Rate
from trainingapps.utils import get_html_mock
from . import path


def test_parse_privatbank(mocker):
    response_mock = [
        {
            "ccy": "USD",
            "base_ccy": "UAH",
            "buy": "00.00000",
            "sale": "00.00000"
        },
        {
            "ccy": "EUR",
            "base_ccy": "UAH",
            "buy": "00.00000",
            "sale": "00.00000"
        },
        {
            "ccy": "TESTFAIL",
            "base_ccy": "TESTFAIL",
            "buy": "00.00000",
            "sale": "00.00000"
        }
    ]

    initial_rate_count = Rate.objects.count()

    mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: response_mock))
    # ^ Return mock

    tasks.parse_privatbank()
    assert Rate.objects.count() == initial_rate_count + 2


def test_parse_monobank(mocker):
    response_mock = [
        {
            "currencyCodeA": 840,
            "currencyCodeB": 980,
            "date": 0000000000,
            "rateBuy": 00.00000,
            "rateSell": 00.00000
        },
        {
            "currencyCodeA": 978,
            "currencyCodeB": 980,
            "date": 0000000000,
            "rateBuy": 00.00000,
            "rateSell": 00.00000
        },
        {
            "currencyCodeA": 'TESTFAIL',
            "currencyCodeB": 'TESTFAIL',
            "date": 0000000000,
            "rateBuy": 00.00000,
            "rateSell": 00.00000
        }
    ]

    initial_rate_count = Rate.objects.count()

    mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: response_mock))

    tasks.parse_monobank()
    assert Rate.objects.count() == initial_rate_count + 2


def test_parse_vkurseua(mocker):
    response_mock = {
        "Dollar": {
            "buy": "00.00000",
            "sale": "00.00000"
        },
        "Euro": {
            "buy": "00.00000",
            "sale": "00.00000"
        },
        "TESTFAIL": {
            "buy": "00.00000",
            "sale": "00.00000"
        }
    }

    initial_rate_count = Rate.objects.count()

    mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: response_mock))

    tasks.parse_vkurseua()
    assert Rate.objects.count() == initial_rate_count + 2


def test_parse_financeua(mocker):
    response_mock = get_html_mock(path.finance_mock)

    mocker.patch(
        'requests.get',
        return_value=MagicMock(
            text=response_mock))

    tasks.parse_financeua()


def test_parse_ukrainekurs(mocker):
    response_mock = get_html_mock(path.kurs_mock)

    mocker.patch(
        'requests.get',
        return_value=MagicMock(
            text=response_mock))

    tasks.parse_ukrainekurs()


def test_parse_bankcreditdnepr(mocker):
    response_mock = get_html_mock(path.creditdnepr_mock)

    mocker.patch(
        'requests.get',
        return_value=MagicMock(
            text=response_mock))

    tasks.parse_bankcreditdnepr()
