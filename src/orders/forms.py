from django import forms
from django.core.validators import RegexValidator

from orders.models import Order, ProductOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "customer_name",
            "phone",
            "extra_message",
            "customer_address",
        )


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = ("order", "product")


class ConfirmationForm(forms.Form):
    name = forms.CharField(required=False)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+************'. Up to 15 digits allowed.",
    )
    phone = forms.CharField(
        validators=[phone_regex], max_length=17
    )  # validators should be a list
    address = forms.CharField(required=False)
    message = forms.CharField(required=False)
