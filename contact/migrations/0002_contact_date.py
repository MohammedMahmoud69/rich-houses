# Generated by Django 4.1 on 2022-09-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
