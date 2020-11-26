from django.db import models


class Profile(models.Model):
    phone_number = models.CharField(
        verbose_name="User number from telegram",
        max_length=13,
        default="00000000000000",
        unique=True,
    )
    name = models.TextField(verbose_name="User name")
    product = models.TextField(verbose_name="products to purchase", blank=True)
    extra_message = models.TextField(
        verbose_name="Some extra text from buyer", blank=True
    )