from rest_framework.test import APIClient
from django.urls import reverse


def test_rates_get():
    client = APIClient()
    response = client.get(reverse('rate-list'))

    assert response.status_code == 200


def test_rates_post():
    client = APIClient()
    response = client.post(reverse('rate-list'), data={})

    assert response.status_code == 400
    assert response.json() == {
        'ccy': ['This field is required.'],

        'buy': ['This field is required.'],
        'sell': ['This field is required.']
    }
