from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from filters.models import *

def main(request):
    filters=Filter.objects.filter(is_active=True)
    return render(request, 'main/index.html', locals())




# class MainPageView(TemplateView, CategoryListMixin):
#     template_name = "index.html"
# Create your views here.
