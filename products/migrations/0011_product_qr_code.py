# Generated by Django 4.1 on 2022-09-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qr_code',
            field=models.ImageField(default='image/default.jpg', upload_to='images/products/qr_codes'),
        ),
    ]
