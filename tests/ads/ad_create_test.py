import pytest
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_create(client, category, user):
    ad = AdFactory.create()

    response = client.post(
        "/ad/create/",
        {
            "name": "test ad name",
            "author_id": user.id,
            "price": 550,
            "description": "test description",
            "is_published": False,
            "category": category.id
        },
        content_type="application/json"
    )

    expected_response = {
        "id": 2,
        "name": "test name",
        "price": 550,
        "description": "test_description",
        "is_published": False,
        "image": ad.image.url if ad.image else None,
        "category": category.id,
        "author_id": '',
    }

    assert response.status_code == 201
    assert response.data == expected_response
