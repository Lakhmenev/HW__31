from django.contrib.auth.models import AbstractUser
from django.db import models
from authentication.validators import nine_years_older, except_rambler
from locations.models import Location


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
