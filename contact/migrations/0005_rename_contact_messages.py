# Generated by Django 4.1 on 2022-09-07 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contact_phone_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Messages',
        ),
    ]