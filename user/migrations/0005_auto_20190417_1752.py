# Generated by Django 2.1.7 on 2019-04-17 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190417_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]