from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponseRedirect

from orders.models import Order, ProductOrder
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from tgbot.forms import RegisterForm, ProfileForm


class ProductOrderOrder(object):
    pass


class UserOrderHistory(LoginRequiredMixin, ListView):

    model = Order
    template_name = 'products/order_list.html'

    def get_queryset(self):
        order = Order.objects.filter(user=self.request.user)
        return ProductOrder.objects.filter(order__in=order).order_by('created')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form, })

# def register(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/")
#     else:
#         form = RegisterForm()
#
#     return render(response, "registration/register.html", {"form": form,})


def profile_update(request):
    try:
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('/')
        else:
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'registration/register.html', {
            'form': profile_form
        })
    except:
        return render(request, 'registration/sorry.html')