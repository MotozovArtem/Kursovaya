from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from brands.models import Brand
from categories.models import Category
from orders.forms import OrderForm

from django.views.generic.base import TemplateView
from django.shortcuts import redirect


# Create your views here.
def basket_adding(req):
    return_dict = dict()
    session_key = req.session.session_key
    # print(req.POST)
    data = req.POST
    filter_id = int(data.get("filter_id"))
    numb = int(data.get("numb"))
    is_delete = data.get("is_delete")
    filter_cat = data.get("filter_name")
    filter_price = data.get("filter_price")
    filter_article = data.get("filter_article")
    cart = req.session.get("cart")
    if not cart:
        req.session["cart"] = []
        req.session["total_price_all_product"] = 0

    if is_delete:
        id = -1
        for i in range(len(req.session["cart"])):
            if cart[i]["filter_id"] == filter_id:
                id = i
        if id >= 0:
            req.session["cart"].pop(id)
    else:
        for item in req.session["cart"]:
            if item["filter_id"] == filter_id:
                if type(item['numb']) is str:
                    item["numb"] = int(item['numb'])
                item["numb"] += numb
                break
        else:
            req.session["cart"].append(
                {"filter_id": filter_id, "filter_cat": filter_cat, "filter_article": filter_article,
                 "filter_price": filter_price, "numb": numb, "is_delete": is_delete})
    req.session.modified = True

    return_dict["products"] = list()
    return_dict["filters_total_numb"] = len(req.session["cart"])
    return_dict["total_price_all_product"] = 0.00
    products_in_session = req.session["cart"]

    for item in products_in_session:
        product_dict = dict()
        product_dict["article"] = item["filter_article"]
        product_dict["id"] = item["filter_id"]
        product_dict["price_per_item"] = item["filter_price"]
        product_dict["name"] = item["filter_cat"]
        product_dict["numb"] = item["numb"]
        product_dict["total_price"] = "{0:.2f}".format(
            float(product_dict["price_per_item"].replace(",", ".")) * int(product_dict["numb"])).replace(".", ",")
        return_dict['products'].append(product_dict)
        return_dict["total_price_all_product"] += float(product_dict["total_price"].replace(",", "."))
    return_dict["total_price_all_product"] = "{0:.2f}".format(return_dict["total_price_all_product"]).replace(".", ",")
    return JsonResponse(return_dict)


def basket_update(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    if data.get("is_delete"):
        i = 0
        while i < len(request.session['cart']):
            if str(request.session['cart'][i].get('filter_id')) in data.getlist("filter_id_list[]"):
                request.session['cart'].pop(i)
            else:
                i += 1
    elif data.get('delete_all'):
        request.session['cart'].clear()
    else:
        filter_id = data.get("filter_id")
        total_price_all_products = 0.00
        for item in request.session['cart']:
            if int(filter_id) == item['filter_id']:
                item['numb'] = data.get('numb')
                item["total_price"] = "{0:.2f}".format(
                    int(item['numb']) * float(item['filter_price'].replace(",", ".")))
            total_price_all_products += float(item['total_price'].replace(",", "."))
        total_price_all_products = "{0:.2f}".format(total_price_all_products).replace(".", ",")
        return_dict['total_price_all_products'] = total_price_all_products
    request.session.modified = True
    return_dict["products"] = list()
    for item in request.session['cart']:
        product_dict = dict()
        product_dict["article"] = item["filter_article"]
        product_dict["id"] = item["filter_id"]
        product_dict["price_per_item"] = item["filter_price"]
        product_dict["name"] = item["filter_cat"]
        product_dict["numb"] = item["numb"]
        product_dict["total_price"] = "{0:.2f}".format(
            float(product_dict["price_per_item"].replace(",", ".")) * int(product_dict["numb"])).replace(".", ",")
        return_dict['products'].append(product_dict)
    return JsonResponse(return_dict)


def checkout(request):
    # Ддя боковых меню
    brands = Brand.objects.order_by("name")
    categorys = Category.objects.order_by("name")
    # *****************************************
    session = request.session.session_key
    return render(request, "checkout/checkout.html", locals())


class PrepareOrder(TemplateView):
    form = None
    template_name = "checkout/prepare_order.html"

    def get(self, request, *args, **kwargs):
        self.form = OrderForm()
        return super(PrepareOrder, self).get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PrepareOrder, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['brands'] = Brand.objects.order_by("name")
        context['categorys'] = Category.objects.order_by("name")
        return context

    def post(self, request, *args, **kwargs):
        self.form = OrderForm(request.POST)
        if self.form.is_valid():
            order = self.form.save()
            for filter_in_cart in request.session['cart']:
                filter = Filter.objects.get(pk=filter_in_cart['filter_id'])
                total_price = "{0:.2f}".format(
                    float(filter_in_cart["filter_price"].replace(",", ".")) *
                    int(filter_in_cart["numb"])
                ).replace(".", ",")
                product_in_order = ProductInOrder.objects.create(order=order, product=filter,
                                                                 numb=filter_in_cart['numb'],
                                                                 price_item=filter_in_cart["filter_price"],
                                                                 total_price=total_price)
            request.session['cart'].clear()
            request.session.modified = True
            return render(request, "checkout/thanks.html", locals())
        else:
            return super(PrepareOrder, self).get(request, *args, **kwargs)
