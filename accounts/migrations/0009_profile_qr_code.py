# Generated by Django 4.1 on 2022-09-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='qr_code',
            field=models.ImageField(blank=True, default='image/default.jpg', null=True, upload_to='images/profiles/qr_codes'),
        ),
    ]
