# Generated by Django 4.1 on 2022-09-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_address_order_address1_order_address2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='situation',
            field=models.CharField(blank=True, choices=[('It was received', 'It was received'), ('In delivery', 'In delivery'), ('In manufacturing', 'In manufacturing')], max_length=200, null=True),
        ),
    ]