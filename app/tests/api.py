# from rest_framework.test import APIClient
from django.urls import reverse


def test_rates_get(api_client_auth):
    # client = APIClient()
    response = api_client_auth.get(reverse('rate-list'))

    assert response.status_code == 200


def test_rates_post(api_client_auth):
    # client = APIClient()
    response = api_client_auth.post(reverse('rate-list'), data={})

    assert response.status_code == 400
    assert response.json() == {
        'ccy': ['This field is required.'],

        'buy': ['This field is required.'],
        'sell': ['This field is required.']
    }


def test_contactus_get(api_client_auth):
    # client = APIClient()
    response = api_client_auth.get(reverse('contactus-list'))

    assert response.status_code == 200
    assert response.request['REQUEST_METHOD'] == 'GET'
    assert response.__dict__['accepted_media_type'] == 'application/json'


def test_contactus_emptydata_post(api_client_auth, mailoutbox):
    # client = APIClient()
    response = api_client_auth.post(reverse('contactus-list'), data={})

    assert response.status_code == 400
    assert response.request['REQUEST_METHOD'] == 'POST'
    assert response.__dict__['accepted_media_type'] == 'application/json'

    assert len(mailoutbox) == 0
    assert response.json() == {
        'email_to': ['This field is required.'],
        'subject': ['This field is required.'],

        'message': ['This field is required.']
    }


def test_contactus_validdata_post(api_client_auth, mailoutbox):
    # client = APIClient()
    data = {
        'email_to': 'valid@email.ru',
        'subject': 'test',

        'message': 'test'
    }

    response = api_client_auth.post(reverse('contactus-list'), data=data)

    assert response.status_code == 201
    assert response.request['REQUEST_METHOD'] == 'POST'
    assert response.__dict__['accepted_media_type'] == 'application/json'

    assert len(mailoutbox) == 1
    assert mailoutbox[0].to[0] == data['email_to']

    del response.json()['id']
    assert response.json() == {
        'email_from': 'eugenepavlov@gmail.com',
        'email_to': 'valid@email.ru',
        'subject': 'test',

        'message': 'test'
    }


def test_contactus_invaliddata_post(api_client_auth, mailoutbox):
    # client = APIClient()
    data = {
        'email_to': 'invalidemailru',
        'subject': '',

        'message': ''
    }

    response = api_client_auth.post(reverse('contactus-list'), data=data)

    assert response.status_code == 400
    assert response.request['REQUEST_METHOD'] == 'POST'
    assert response.__dict__['accepted_media_type'] == 'application/json'

    assert len(mailoutbox) == 0
    assert response.json() == {
        'email_to': ['Enter a valid email address.'],
        'subject': ['This field may not be blank.'],

        'message': ['This field may not be blank.']
    }
