from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
class MainPageView(TemplateView, CategoryListMixin):
    template_name = "index.html"
# Create your views here.
