# Generated by Django 4.2.1 on 2023-05-03 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0006_alter_user_profile_gender_alter_user_profile_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='user',
        ),
    ]
