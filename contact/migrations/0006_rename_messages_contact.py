# Generated by Django 4.1 on 2022-09-19 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_rename_contact_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Contact',
        ),
    ]
