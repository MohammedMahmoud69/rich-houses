# Generated by Django 4.1 on 2022-09-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qr_code',
            field=models.ImageField(blank=True, default='image/default.jpg', null=True, upload_to='images/products/qr_codes'),
        ),
    ]
