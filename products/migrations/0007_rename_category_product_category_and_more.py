# Generated by Django 4.1 on 2022-08-31 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_slug_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Describtion',
            new_name='describtion',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
    ]