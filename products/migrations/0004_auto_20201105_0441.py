# Generated by Django 3.1.2 on 2020-11-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]