# Generated by Django 2.1.5 on 2019-03-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190305_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='first_year_first_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='first_year_second_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='first_year_summer_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fourth_year_first_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fourth_year_second_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='second_year_first_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='second_year_second_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='second_year_summer_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='third_year_first_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='third_year_second_semester_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='third_year_summer_bsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=100)),
                ('descriptive_title', models.CharField(max_length=100)),
                ('requisite', models.CharField(blank=True, max_length=100)),
                ('lecture', models.CharField(max_length=100)),
                ('lab', models.CharField(blank=True, max_length=100)),
                ('no_of_units', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='bsa',
        ),
    ]