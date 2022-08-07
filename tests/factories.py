import factory.django

from ads.models import Ad
from categories.models import Category
from authentication.models import User
from selections.models import Selection


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.Faker("word")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email_address = factory.Faker("email")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 550
    

class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "Selection_Name"
    owner_id = 1
