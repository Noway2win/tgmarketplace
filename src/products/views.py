from django.shortcuts import render
from django.views.generic import ListView, DetailView

from orders.forms import OrderForm
from orders.models import ProductOrder
from products.models import ProductImage, Product


class IndexView(ListView):
    queryset = ProductImage.objects.filter(is_active=True, is_main=True)
    template_name = "products/index.html"


class Detailed_Prod(DetailView):
    model = ProductImage

    def session_key(self):
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.cycle_key()

        return session_key


def gretting_view(request):
    return render(request, "products/regards_for_order.html")
