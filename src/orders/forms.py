from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "customer_name",
            "phone_number",
            "extra_message",
            "is_active",
        )

