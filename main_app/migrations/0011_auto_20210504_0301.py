# Generated by Django 3.2 on 2021-05-04 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='location',
            new_name='proLoc',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='proName',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='occupation',
            new_name='proOcc',
        ),
    ]
