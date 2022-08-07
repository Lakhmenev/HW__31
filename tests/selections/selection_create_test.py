import pytest


@pytest.mark.django_db
def test_selection_create(client, user_token, user, ad):
    response = client.post(
        "selections/create/",
        {
            "name": "test selections name",
            "owner": user.id,
            "items": [ad.id]
        },
        content_type='application/json',
        HTTP_AUTHORIZATION=f"Bearer {user_token}"
    )

    expected_response = {
        "id": 1,
        "name": "test selections name",
        "owner": user.id,
        "items": [ad.id]
    }

    assert response.status_code == 201
    assert response.data == expected_response
