# Generated by Django 3.0.4 on 2020-12-23 08:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daftarGuide', '0002_auto_20201221_0258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guide',
            new_name='GuideModel',
        ),
    ]
