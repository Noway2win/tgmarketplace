from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import ProductImage, Product


class IndexView(ListView):
    queryset = ProductImage.objects.filter(is_active=True, is_main=True)
    template_name = "products/index.html"


class Detailed_Prod(DetailView
                    ):
    model = ProductImage