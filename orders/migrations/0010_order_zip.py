# Generated by Django 4.1 on 2022-09-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.IntegerField(default=0, max_length=7),
            preserve_default=False,
        ),
    ]
