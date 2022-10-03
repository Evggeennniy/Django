from django.urls import reverse


def test_index_get(client):
    response = client.get(reverse('main'))

    assert response.status_code == 200
