# Generated by Django 3.0.1 on 2020-04-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0004_auto_20200322_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='month',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
