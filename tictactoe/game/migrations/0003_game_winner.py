# Generated by Django 5.0.7 on 2024-08-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
