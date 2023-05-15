# Generated by Django 4.2.1 on 2023-05-15 03:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+962\\d{9}$')], verbose_name='phone no.'),
        ),
    ]
