# Generated by Django 5.0.7 on 2024-08-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustom',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='images/avatars/'),
        ),
    ]
