from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from locations.models import Location


def nine_years_older(value):
    if (date.today().year - value.year) < 9:
        raise ValidationError("Your age must be over 9 years old.")


def except_rambler(value):
    domain_name = value.split('@')
    if 'rambler' in domain_name[1]:
        raise ValidationError("Registration with Rambler is prohibited.")


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    locations = models.ManyToManyField(Location)
    role = models.CharField(max_length=9, choices=ROLES, default="member")
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, validators=[nine_years_older])
    email_address = models.EmailField(unique=True, validators=[except_rambler])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
