from django.forms import ModelForm
from django import forms

from filters.models import Filter
from brands.models import Brand
from categories.models import Category
from orders.models import *


class FilterForm(ModelForm):
    class Meta:
        model = Filter
        fields = ["article", "category", "brand", "price", "discount", "description", "specific",
                  "is_active", "is_popular", "is_new"]

    article = forms.CharField(label="Артикул")
    is_active = forms.CheckboxInput()
    is_popular = forms.CheckboxInput()
    is_new = forms.CheckboxInput()


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "is_active"]

    # name = forms.CharField(label="Название")
    is_active = forms.CheckboxInput()


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "customer_phone", "customer_email", "total_price", "status", "comments"]


class ProductInOrderForm(ModelForm):
    class Meta:
        model = ProductInOrder
        fields= ["product", "numb"]
