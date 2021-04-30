# Generated by Django 3.2 on 2021-04-30 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentBody', models.CharField(max_length=250)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.carpost')),
            ],
        ),
    ]
