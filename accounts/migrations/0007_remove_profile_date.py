# Generated by Django 4.1 on 2022-08-27 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Date',
        ),
    ]
