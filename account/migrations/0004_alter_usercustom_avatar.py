# Generated by Django 5.0.7 on 2024-08-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_image_usercustom_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustom',
            name='avatar',
            field=models.ImageField(default='default/avatar.jpg', upload_to='images/avatars/'),
        ),
    ]
