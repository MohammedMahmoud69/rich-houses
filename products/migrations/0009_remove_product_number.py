# Generated by Django 4.1 on 2022-09-04 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='number',
        ),
    ]
