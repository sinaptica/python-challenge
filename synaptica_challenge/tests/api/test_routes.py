import json
import pytest
from rest_framework.test import APIRequestFactory
from rest_framework import status
from synaptica_challenge.api.models import Item
from django.urls import reverse
from synaptica_challenge.api.views import ItemDetail



@pytest.mark.django_db
def test_post_item(client):
    expected_response = {
        'id': 1,
        'name': 'test item 1',
        'description': 'test description 1'
    }

    url = "/api/items"

    response = client.post(
        url,
        {
            'id': 1,
            'name': 'test item 1',
            'description': 'test description 1'
        },
        format='json'
    )

    assert response.status_code == 201
    assert json.loads(response.content) == expected_response



@pytest.mark.django_db
def test_get_item(client):
    Item.objects.create(id=1, name="test item 1", description="test description 1")
    assert Item.objects.count() == 1

    expected_response = {
        'id': 1,
        'name': 'test item 1',
        'description': 'test description 1'
    }

    url = "/api/items/1/"

    response = client.get(url)

    assert response.status_code == 200
    assert json.loads(response.content) == expected_response


@pytest.mark.django_db
def test_list_items(client):
    Item.objects.create(id=1, name="test item 1", description="test description 1")
    Item.objects.create(id=2, name="test item 2", description="test description 2")
    assert Item.objects.count() == 2

    expected_response = [
        {
            'id': 1,
            'name': 'test item 1',
            'description': 'test description 1'
        },
        {
            'id': 2,
            'name': 'test item 2',
            'description': 'test description 2'
        },
    ]
    url = "/api/items"

    response = client.get(url)

    assert response.status_code == 200
    assert json.loads(response.content) == expected_response


@pytest.mark.django_db
def test_update_item(client):
    Item.objects.create(id=1, name="test item 1", description="test description 1")
    assert Item.objects.count() == 1

    get_expected_response = {
        'id': 1,
        'name': 'test item 1',
        'description': 'test description 1'
    }

    url = "/api/items/1/"

    get_response = client.get(url)

    assert get_response.status_code == 200
    assert json.loads(get_response.content) == get_expected_response

    update_expected_response = {
        'id': 1,
        'name': 'test item 1 updated',
        'description': 'test description 1 updated'
    }

    # Very ugly magic that had to be done in order to make the PUT test pass
    factory = APIRequestFactory()
    request = factory.put(
        url,
        {"id": 1, "name": "test item 1 updated", "description": "test description 1 updated"}
    )
    item_view = ItemDetail.as_view()
    update_response = item_view(request, pk=1).render()

    assert update_response.status_code == 200
    assert json.loads(update_response.content) == update_expected_response

