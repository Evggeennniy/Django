from django.urls import reverse
# import pytest


def test_contactus_get(client):
    response = client.get(reverse('contactus_list'))

    assert response.status_code == 200


# @pytest.mark.parametrize('from_email', ('email0', 'email1', 'email2'))
# # ^ While for every params
# def test_contactus_post_invalid_email(client, from_email):
#     data = {
#         'email_from': from_email,
#         'subject': 'subject',
#         'body': 'body'
#     }
#     response = client.get(reverse('contactus_create'), data=data)
#     assert response.status_code == 200
