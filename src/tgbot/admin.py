from django.contrib import admin

from tgbot.models import Profile


@admin.register(Profile)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]

    class Meta:
        model = Profile
