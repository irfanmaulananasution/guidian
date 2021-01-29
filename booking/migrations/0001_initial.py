# Generated by Django 3.1.2 on 2020-12-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('participants', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('show', models.BooleanField()),
                ('token', models.CharField(max_length=25)),
            ],
        ),
    ]
