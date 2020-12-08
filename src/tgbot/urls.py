from django.urls import path, include

from tgbot import views
from tgbot.views import register, profile_update

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("order_history/", views.UserOrderHistory.as_view(), name="order_history"),
    path("update_profile/", profile_update, name="update_profile"),
]
