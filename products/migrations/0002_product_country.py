# Generated by Django 3.1.2 on 2020-11-05 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]