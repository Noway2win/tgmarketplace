from django.contrib import admin
from .models import Profile, Product
from .forms import ProfileForm

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "name", "purchase", "product", "extra_message")
    form = ProfileForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_type",
        "product_name",
        "product_price",
        "product_description",
    )
    list_filter = ("product_type",)
    search_fields = ("product_name",)


