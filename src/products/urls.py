from django.urls import path

from orders.views import basket_add
from products import views
from products.apps import ProductsConfig

app_name = ProductsConfig.label


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.Detailed_Prod.as_view(), name="product"),
    path("basket_add", basket_add, name="basket"),
]