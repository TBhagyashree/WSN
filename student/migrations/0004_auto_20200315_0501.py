# Generated by Django 3.0.1 on 2020-03-15 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200315_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='Student_card',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
