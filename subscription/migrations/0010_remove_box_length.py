# Generated by Django 3.1.2 on 2020-11-26 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0009_auto_20201126_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='length',
        ),
    ]
