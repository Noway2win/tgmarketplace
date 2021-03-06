# Generated by Django 3.1.3 on 2020-11-21 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_type", models.TextField(verbose_name="type of product")),
                ("product_name", models.TextField(verbose_name="name of product")),
                ("is_active", models.BooleanField(default=True)),
                (
                    "product_price",
                    models.PositiveIntegerField(verbose_name="price of product"),
                ),
                (
                    "product_description",
                    models.TextField(blank=True, verbose_name="description of product"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="prod_images/")),
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Photo",
                "verbose_name_plural": "Photos",
            },
        ),
    ]
