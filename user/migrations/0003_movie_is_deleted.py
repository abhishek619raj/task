# Generated by Django 2.1.7 on 2019-04-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]