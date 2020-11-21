from django.contrib import admin

# Register your models here.
from orders.forms import OrderForm
from orders.models import Order, ProductOrder


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductOrderInline]
    form = OrderForm


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductOrder._meta.fields]

    class Meta:
        model = ProductOrder
