from django.contrib import admin
from .models import Profile
from .forms import ProfileForm

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "name", "purchase", "product", "extra_message")
    form = ProfileForm
