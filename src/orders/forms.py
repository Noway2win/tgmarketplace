from django import forms

from orders.models import Order, ProductOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "customer_name",
            "phone_number",
            "extra_message",
            "is_active",
        )


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = ("order", "product")
