from filters.models import *
from orders.models import *
from django.shortcuts import render, redirect
from .forms import *
from django.utils.datastructures import MultiValueDictKeyError

def myadmin(req):
    return render(req, "Admin/admin_base.html", locals())


def product(req):
    filter_list = Filter.objects.all()
    return render(req, "Admin/print_filter.html", locals())


def brands(req):
    brand_list = Brand.objects.all()
    return render(req, "Admin/print_brand.html", locals())


def categories(req):
    category_list = Category.objects.all()
    return render(req, "Admin/print_cat.html", locals())

def orders(req):
    order_list = Order.objects.all()
    return render(req, "Admin/print_order.html", locals())


def filter_del(request):
    obj = Filter.objects.all()
    if request.method == "POST":
        try:
            filter_select = request.POST.getlist("del")
        except MultiValueDictKeyError:
            filter_select = []
        if filter_select:
            for i in obj:
                if str(i.id_filter) in filter_select:
                    i.delete()
            return redirect("admin_filter")
        else:
            return redirect("admin_filter")
    else:
        return render(request, "admin/print_filter.html", locals())


def brand_del(request):
    obj = Brand.objects.all()

    if request.method == "POST":

        try:
            brand_select = request.POST.getlist("del")
        except MultiValueDictKeyError:
            brand_select = []
        if brand_select:
            for i in obj:
                if str(i.id_brand) in brand_select:
                    i.delete()
            return redirect("admin_brand")
        else:
            return redirect("admin_brand")
    else:
        return render(request, "admin/print_brand.html", locals())


def cat_del(request):
    obj = Category.objects.all()
    if request.method == "POST":
        try:
            cat_select = request.POST.getlist("del")
        except MultiValueDictKeyError:
            cat_select = []
        if cat_select:
            for i in obj:
                if str(i.id_category) in cat_select:
                    i.delete()
            return redirect("admin_cat")
        else:
            return redirect("admin_cat")
    else:
        return render(request, "admin/print_cat.html", locals())

def order_del(request):
    obj = Order.objects.all()
    if request.method == "POST":
        try:
            order_select = request.POST.getlist("del")
        except MultiValueDictKeyError:
            order_select = []
        if order_select:
            for i in obj:
                if str(i.id_order) in order_select:
                    i.delete()
            return redirect("admin_order")
        else:
            return redirect("admin_order")
    else:
        return render(request, "admin/print_order.html", locals())

def order_detail(request, id):
    products_in_order_list = ProductInOrder.objects.filter(order__id_order=id)
    return render(request, "Admin/print_products_in_order.html", locals())