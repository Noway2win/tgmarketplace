from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=128)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+************'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    extra_message = models.TextField(
        verbose_name="Some extra text from buyer", blank=True
    )
    customer_address = models.CharField(
        verbose_name="Customer address",
        max_length=128,
        blank=True,
        null=True,
        default=None,
    )

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ProductOrder(models.Model):
    order = models.ForeignKey(
        Order, blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField(
        default=0, verbose_name="price in order", max_digits=5, decimal_places=2
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "ProductOrder"
        verbose_name_plural = "ProductOrders"

    def save(self, *args, **kwargs):
        product_price = self.product.product_price
        self.price = product_price  # * self.
        # self.price.save(force_update=True)
        super(ProductOrder, self).save(*args, **kwargs)


class ProductBasket(models.Model):
    session_key = models.CharField(max_length=128, default=None)
    order = models.ForeignKey(
        Order, blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, blank=True, null=True, default=None, on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField(
        default=0, verbose_name="price in order", max_digits=5, decimal_places=2
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.product_name

    class Meta:
        verbose_name = "ProductInBasket"
        verbose_name_plural = "ProductInBasket"

    def save(self, *args, **kwargs):
        product_price = self.product.product_price
        self.price = product_price  # * self.
        # self.price.save(force_update=True)
        super(ProductBasket, self).save(*args, **kwargs)
