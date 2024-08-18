# Generated by Django 5.0.7 on 2024-08-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_goal_is_use_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at', 'type']},
        ),
        migrations.AlterField(
            model_name='goal',
            name='current_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='goal',
            name='target_amount',
            field=models.FloatField(),
        ),
    ]