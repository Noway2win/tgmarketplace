# Generated by Django 3.1.3 on 2020-11-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_auto_20201121_1707"),
    ]

    operations = [
        migrations.AddField(
            model_name="productorder",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=5, verbose_name="price in order"
            ),
        ),
    ]
