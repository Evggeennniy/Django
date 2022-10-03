from django.urls import reverse


def test_source_get(client):
    response = client.get(reverse('source_list'))

    assert response.status_code == 302
