import pytest
# from django.core.management import call_command
# from rest_framework.test import APIClient


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