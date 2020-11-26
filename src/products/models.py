from PIL import Image
from django.db import models

# Create your models here.
from django.urls import reverse_lazy
from tgbot import TgbotConfig

class Product(models.Model):
    class Prod_Type(models.TextChoices):
        Pictures = "P"
        Logos = "L"

    product_type = models.TextField(
        choices=Prod_Type.choices, verbose_name="type of product"
    )
    product_name = models.TextField(verbose_name="name of product", unique=True)
    is_active = models.BooleanField(default=True)
    product_price = models.PositiveIntegerField(verbose_name="price of product")
    product_description = models.TextField(
        verbose_name="description of product", blank=True
    )
    created = models.DateTimeField(
        verbose_name="Date and time of creation", auto_now_add=True, auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Date and time of creation", auto_now_add=False, auto_now=True
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return "%s %s" % (self.product_name, self.product_price)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="prod_images/")
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse_lazy("products:product", kwargs={"pk": self.pk})
