# Generated by Django 2.1.5 on 2019-03-07 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_first_year_first_semester_bsn_first_year_first_semester_math_first_year_second_semester_bsn_first_ye'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='first_year_first_semester_bsa',
            options={'verbose_name': 'BSA = First Year First Semester', 'verbose_name_plural': 'BSA = First Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='first_year_first_semester_bsn',
            options={'verbose_name': 'BSN = First Year First Semester', 'verbose_name_plural': 'BSN = First Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='first_year_first_semester_math',
            options={'verbose_name': 'LAED-MATH = First Year First Semester', 'verbose_name_plural': 'LAED-MATH = First Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='first_year_second_semester_bsa',
            options={'verbose_name': 'BSA = First Year Second Semester', 'verbose_name_plural': 'BSA = First Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='first_year_second_semester_bsn',
            options={'verbose_name': 'BSN = First Year Second Semester', 'verbose_name_plural': 'BSN = First Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='first_year_second_semester_math',
            options={'verbose_name': 'LAED-MATH = First Year Second Semester', 'verbose_name_plural': 'LAED-MATH = First Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='first_year_summer_bsa',
            options={'verbose_name': 'BSA = First Year Summer', 'verbose_name_plural': 'BSA = First Year Summer'},
        ),
        migrations.AlterModelOptions(
            name='first_year_summer_bsn',
            options={'verbose_name': 'BSN = First Year Summer', 'verbose_name_plural': 'BSN = First Year Summer'},
        ),
        migrations.AlterModelOptions(
            name='fourth_year_first_semester_bsa',
            options={'verbose_name': 'BSA = Fourth Year First Semester', 'verbose_name_plural': 'BSA = Fourth Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='fourth_year_first_semester_bsn',
            options={'verbose_name': 'BSN = Fourth Year First Semester', 'verbose_name_plural': 'BSN = Fourth Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='fourth_year_first_semester_math',
            options={'verbose_name': 'LAED-MATH = Fourth Year First Semester', 'verbose_name_plural': 'LAED-MATH = Fourth Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='fourth_year_second_semester_bsa',
            options={'verbose_name': 'BSA = Fourth Year Second Semester', 'verbose_name_plural': 'BSA = Fourth Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='fourth_year_second_semester_bsn',
            options={'verbose_name': 'BSN = Fourth Year Second Semester', 'verbose_name_plural': 'BSN = Fourth Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='fourth_year_second_semester_math',
            options={'verbose_name': 'LAED-MATH = Fourth Year Second Semester', 'verbose_name_plural': 'LAED-MATH = Fourth Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='second_year_first_semester_bsa',
            options={'verbose_name': 'BSA = Second Year First Semester', 'verbose_name_plural': 'BSA = Second Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='second_year_first_semester_bsn',
            options={'verbose_name': 'BSN = Second Year First Semester', 'verbose_name_plural': 'BSN = Second Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='second_year_first_semester_math',
            options={'verbose_name': 'LAED-MATH = Second Year First Semester', 'verbose_name_plural': 'LAED-MATH = Second Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='second_year_second_semester_bsa',
            options={'verbose_name': 'BSA = Second Year Second Semester', 'verbose_name_plural': 'BSA = Second Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='second_year_second_semester_bsn',
            options={'verbose_name': 'BSN = Second Year Second Semester', 'verbose_name_plural': 'BSN = Second Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='second_year_second_semester_math',
            options={'verbose_name': 'LAED-MATH = Second Year Second Semester', 'verbose_name_plural': 'LAED-MATH = Second Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='second_year_summer_bsa',
            options={'verbose_name': 'BSA = Second Year Summer', 'verbose_name_plural': 'BSA = Second Year Summer'},
        ),
        migrations.AlterModelOptions(
            name='second_year_summer_bsn',
            options={'verbose_name': 'BSN = Second Year Summer', 'verbose_name_plural': 'BSN = Second Year Summer'},
        ),
        migrations.AlterModelOptions(
            name='third_year_first_semester_bsa',
            options={'verbose_name': 'BSA = Third Year First Semester', 'verbose_name_plural': 'BSA = Third Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='third_year_first_semester_bsn',
            options={'verbose_name': 'BSN = Third Year First Semester', 'verbose_name_plural': 'BSN = Third Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='third_year_first_semester_math',
            options={'verbose_name': 'LAED-MATH = Third Year First Semester', 'verbose_name_plural': 'LAED-MATH = Third Year First Semester'},
        ),
        migrations.AlterModelOptions(
            name='third_year_second_semester_bsa',
            options={'verbose_name': 'BSA = Third Year Second Semester', 'verbose_name_plural': 'BSA = Third Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='third_year_second_semester_bsn',
            options={'verbose_name': 'BSN = Third Year Second Semester', 'verbose_name_plural': 'BSN = Third Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='third_year_second_semester_math',
            options={'verbose_name': 'LAED-MATH = Third Year Second Semester', 'verbose_name_plural': 'LAED-MATH = Third Year Second Semester'},
        ),
        migrations.AlterModelOptions(
            name='third_year_summer_bsa',
            options={'verbose_name': 'BSA = Third Year Summer', 'verbose_name_plural': 'BSA = Third Year Summer'},
        ),
        migrations.AddField(
            model_name='first_year_first_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='first_year_second_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='first_year_summer_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='fourth_year_first_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='fourth_year_second_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='second_year_first_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='second_year_second_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='second_year_summer_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='third_year_first_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='third_year_second_semester_bsn',
            name='lab',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
