# Generated by Django 5.0.6 on 2024-06-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='owned_guilds',
            field=models.IntegerField(default=0),
        ),
    ]
