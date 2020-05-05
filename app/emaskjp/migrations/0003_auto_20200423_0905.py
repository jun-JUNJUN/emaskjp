# Generated by Django 3.0.3 on 2020-04-23 09:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emaskjp', '0002_auto_20200423_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='prefecture',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='都道府県'),
        ),
    ]
