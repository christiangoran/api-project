# Generated by Django 3.2.20 on 2023-09-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_y7ymw3', upload_to='images/'),
        ),
    ]
