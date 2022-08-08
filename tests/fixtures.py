import pytest


@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = 'dilan'
    password = 'dilan12345'
    role = "moderator"

    django_user_model.objects.create_user(username=username, password=password, role=role)
    response = client.post("/user/token/", {"username": username, "password": password}, format='json')
    
    return response.data['access']
