# Generated by Django 3.0.1 on 2020-03-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='Time_of_arrival',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='Today_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]