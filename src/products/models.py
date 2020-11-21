from django.db import models

# Create your models here.


class Product(models.Model):
    product_type = models.TextField(verbose_name="type of product")
    product_name = models.TextField(verbose_name="name of product", unique=True)
    is_active = models.BooleanField(default=True)
    # product_image = models.ImageField(verbose_name="image of product")
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
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
