# Generated by Django 4.1 on 2022-10-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_aboutas_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subject', models.TextField()),
                ('img', models.ImageField(default='images/default.jpg', upload_to='images/about_us')),
            ],
        ),
        migrations.DeleteModel(
            name='AboutAs',
        ),
    ]
