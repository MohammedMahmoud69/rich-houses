# Generated by Django 4.1 on 2022-08-31 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Slug',
            new_name='slug',
        ),
    ]