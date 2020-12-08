from django.contrib import admin

# Register your models here.
from orders.forms import OrderForm
from orders.models import Order, ProductOrder, ProductBasket


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductOrderInline]
    form = OrderForm
    readonly_fields = ["user"]


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductOrder._meta.fields]

    class Meta:
        model = ProductOrder


@admin.register(ProductBasket)
class ProductBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductBasket._meta.fields]

    class Meta:
        model = ProductBasket
