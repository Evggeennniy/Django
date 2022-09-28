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


def test_contactus_get():
    client = APIClient()
    response = client.get(reverse('contactus-list'))

    assert response.status_code == 200
    assert response.request['REQUEST_METHOD'] == 'GET'
    assert response.__dict__['accepted_media_type'] == 'application/json'


def test_contactus_emptydata_post(mailoutbox):
    client = APIClient()
    response = client.post(reverse('contactus-list'), data={})

    assert response.status_code == 400
    assert response.request['REQUEST_METHOD'] == 'POST'
    assert response.__dict__['accepted_media_type'] == 'application/json'

    assert len(mailoutbox) == 0
    assert response.json() == {
        'email_to': ['This field is required.'],
        'subject': ['This field is required.'],

        'message': ['This field is required.']
    }


def test_contactus_validdata_post(mailoutbox):
    client = APIClient()
    data = {
        'email_to': 'valid@email.ru',
        'subject': 'test',

        'message': 'test'
    }

    response = client.post(reverse('contactus-list'), data=data)

    assert response.status_code == 201
    assert response.request['REQUEST_METHOD'] == 'POST'
    assert response.__dict__['accepted_media_type'] == 'application/json'

    assert len(mailoutbox) == 1  # Create & Send
    assert mailoutbox[0].to[0] == data['email_to']

    del response.json()['id']
    assert response.json() == {
        'email_from': 'eugenepavlov@gmail.com',
        'email_to': 'valid@email.ru',
        'subject': 'test',

        'message': 'test'
    }


def test_contactus_invaliddata_post(mailoutbox):
    client = APIClient()
    data = {
        'email_to': 'invalidemailru',
        'subject': '',

        'message': ''
    }

    response = client.post(reverse('contactus-list'), data=data)

    assert response.status_code == 400
    assert response.request['REQUEST_METHOD'] == 'POST'
    assert response.__dict__['accepted_media_type'] == 'application/json'

    assert len(mailoutbox) == 1  # Create & Not send
    assert response.json() == {
        'email_to': ['Enter a valid email address.'],
        'subject': ['This field may not be blank.'],

        'message': ['This field may not be blank.']
    }
