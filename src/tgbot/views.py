from django.shortcuts import render

from products.models import Product, ProductImage
from .forms import ProfileForm


def index(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, "tgbot/index.html", locals())
