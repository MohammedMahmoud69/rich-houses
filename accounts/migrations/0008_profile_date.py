# Generated by Django 4.1 on 2022-08-27 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]