# Generated by Django 4.0.5 on 2022-10-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0004_remove_product_status_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_inventory_count',
            field=models.IntegerField(default=0),
        ),
    ]