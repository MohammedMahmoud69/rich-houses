# Generated by Django 4.1 on 2022-10-21 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_rename_address2_order_address_remove_order_address1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(5)]),
        ),
    ]
