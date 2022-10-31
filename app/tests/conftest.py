import pytest
from rest_framework.test import APIClient
# from django.core.management import call_command
# from rest_framework.test import APIClient
from accounts.models import User
from django.urls import reverse


@pytest.fixture(autouse=True, scope='function')
def enable_db_access_for_all_tests(db):
    """
    Give access to database for all tests
    """

# @pytest.fixture(autouse=True, scope='session')
# def load_fixtures(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         fixtures = (
#             'source.json',
#             'rates.json'
#         )
#         # ^ Create tuple of files
#         for fixture in fixtures:
#             call_command('loaddata', f'app/tests/fixtures/{fixture}')
# # ^ For load db fixtures


@pytest.fixture()
def api_client():
    return APIClient()
# Create fixrutes api_client


@pytest.fixture()
def api_client_auth(api_client):
    password = 'test'
    email = 'test@test.com'
    user = User(email=email)
    user.set_password(password)
    user.save()
    # ^ Create user

    response = api_client.post(
        reverse('token_obtain_pair'),
        data={'email': email, 'password': password}
    )
    # ^ Get access token

    assert response.status_code == 200, response.content
    assert 'access' in response.json(), response.content
    # ^ Check a complete

    token = response.json()['access']
    api_client.credentials(
        HTTP_AUTHORIZATION=f'JWT {token}'
    )
    # ^ Get and set headers

    return api_client
# ^ Fixtures auth users
