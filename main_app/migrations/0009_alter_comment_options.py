# Generated by Django 3.2 on 2021-05-01 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_carpost_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
    ]
