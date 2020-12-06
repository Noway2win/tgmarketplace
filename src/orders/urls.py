from django.urls import path

from orders.apps import OrdersConfig
from orders.views import basket_add

app_name = OrdersConfig.name
