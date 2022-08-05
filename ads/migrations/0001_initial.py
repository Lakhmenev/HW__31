# Generated by Django 4.1 on 2022-08-05 12:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)])),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ads/')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
