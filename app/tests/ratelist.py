from django.urls import reverse


def test_rate_get(client):
    response = client.get(reverse('rate_list'))

    assert response.status_code == 302
