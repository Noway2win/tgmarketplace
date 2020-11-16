from django.db import models


class Profile(models.Model):
    phone_number = models.CharField(verbose_name="User number from telegram", max_length=13, default="00000000000000")
    name = models.TextField(verbose_name="User name")
    purchase = models.BooleanField(default=False)
    product = models.TextField(verbose_name="products to purchase", blank=True)
    extra_message = models.TextField(verbose_name="Some extra text from buyer", blank=True)



class Meta:
    verbose_name = "Profile"

class Product(models.Model):
    product_type = models.TextField(verbose_name="type of product")
    product_name = models.TextField(verbose_name="name of product")
    product_price = models.PositiveIntegerField(verbose_name="price of product")
    product_description = models.TextField(verbose_name="description of product", blank=True)