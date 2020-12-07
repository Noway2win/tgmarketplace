# from django.shortcuts import render
# from django.views.generic import DetailView, ListView
# from products.models import Product, ProductImage
# from .forms import ProfileForm
#
#
# def index(request):
#     products_images = ProductImage.objects.filter(is_active=True, is_main=True)
#     return render(request, "tgbot/index.html", locals())
#
#
# class IndexView(ListView):
#     queryset = ProductImage.objects.filter(is_active=True, is_main=True)
#     template_name = "tgbot/index.html"
#
#
# class detailed_prod(DetailView):
#     model = Product
