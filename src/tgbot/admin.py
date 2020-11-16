from django.contrib import admin
from .models import Profile
from .forms import ProfileForm
from .models import Product
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "name", "purchase", "product", "extra_message")
    form = ProfileForm


@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ("product_type", "product_name", "product_price", "product_description")
