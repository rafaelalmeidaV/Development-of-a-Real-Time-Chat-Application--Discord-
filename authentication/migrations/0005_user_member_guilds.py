# Generated by Django 5.0.6 on 2024-06-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_owned_guilds'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='member_guilds',
            field=models.IntegerField(default=0),
        ),
    ]