# Generated by Django 3.1.2 on 2020-12-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regularTour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulartourmodel',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
