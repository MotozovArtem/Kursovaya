from orders.models import Order
from django.forms import ModelForm
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "customer_email", "customer_phone", "comments"]
    