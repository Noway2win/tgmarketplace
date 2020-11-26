from django.urls import path

from tgbot import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.detailed_prod.as_view(), name="product"),
]
