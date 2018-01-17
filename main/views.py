from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from filters.models import *
from brands.models import *
from categories.models import *


def main(request):
    # filter_list =FilterImage.objects.filter(filter__is_active=True).order_by("created") #Фильтры отсорт по дате добавления
    popular_filter_list=FilterImage.objects.filter(filter__is_popular=True, is_main=True, is_active=True, filter__is_active=True)
    popular_filter=popular_filter_list[0:7]
    new_filter_list=FilterImage.objects.filter(is_active=True, is_main=True, filter__is_new=True, filter__is_active=True)
    new_filter=new_filter_list[0:7]
    brands_image_list=BrandImage.objects.filter(is_active=True, is_main=True, brand__is_active=True)
    filter_sale_list=FilterImage.objects.filter(is_active=True, is_main=True, filter__discount__gt=0, filter__is_active=True)
    filter_sale=filter_sale_list[0:4]
    #Ддя боковых меню
    brands=Brand.objects.order_by("name")
    categorys=Category.objects.order_by("name")
    #*****************************************
    return render(request, 'main/index.html', locals())


