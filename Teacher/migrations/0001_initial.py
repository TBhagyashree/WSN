# Generated by Django 3.0.1 on 2020-03-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=10)),
                ('lec1', models.CharField(max_length=50)),
                ('lec2', models.CharField(max_length=50)),
                ('lec3', models.CharField(max_length=50)),
                ('lec4', models.CharField(max_length=50)),
                ('lec5', models.CharField(max_length=50)),
                ('lec6', models.CharField(max_length=50)),
            ],
        ),
    ]
