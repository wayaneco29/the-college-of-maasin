# Generated by Django 2.1.5 on 2019-01-29 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_delete_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
