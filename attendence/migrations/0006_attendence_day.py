# Generated by Django 3.0.1 on 2020-04-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0005_attendence_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='day',
            field=models.CharField(max_length=10, null=True),
        ),
    ]