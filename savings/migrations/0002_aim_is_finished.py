# Generated by Django 3.1.2 on 2020-10-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aim',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]