# Generated by Django 2.1.5 on 2019-03-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190307_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForSMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
    ]