# Generated by Django 3.1.3 on 2020-11-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_auto_20201121_1707"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_type",
            field=models.TextField(
                choices=[("P", "Picrures"), ("L", "Logos")],
                verbose_name="type of product",
            ),
        ),
    ]
