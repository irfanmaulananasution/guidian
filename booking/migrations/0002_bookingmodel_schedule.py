# Generated by Django 3.1.2 on 2020-12-27 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schedule.regtourschedulemodel'),
            preserve_default=False,
        ),
    ]
