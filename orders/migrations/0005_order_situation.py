# Generated by Django 4.1 on 2022-09-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='situation',
            field=models.CharField(choices=[('It was received', 'It was received'), ('In delivery', 'In delivery'), ('In manufacturing', 'In manufacturing')], default='In manufacturing', max_length=200),
            preserve_default=False,
        ),
    ]
