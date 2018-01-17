from django.shortcuts import render
from filters.models import *
from categories.models import *
from brands.models import *
from orders.models import *
from django.core.paginator import Paginator, InvalidPage
from django.utils.datastructures import MultiValueDictKeyError


def top(req):
    filter_top_list = Filter.objects.all()

    return render(req, "main/top.html", locals())


def filter_of_category(req, id):
    # Ддя боковых меню
    brands = Brand.objects.order_by("name")
    categorys = Category.objects.order_by("name")
    # *****************************************
    all_brands = Brand.objects.all()
    cat = Category.objects.get(id_category=id)
    try:
        page_num = req.GET["page"]
    except KeyError:
        page_num = 1

    try:
        pag = req.GET["pag"]
        has_pag = True
    except MultiValueDictKeyError:
        has_pag = False
        pag = 20

    try:
        sort = req.GET["sort"]
        has_sort = True
    except MultiValueDictKeyError:
        sort = "default"
        has_sort = False

    if sort == "price_asc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat).order_by("filter__price"), pag)
    elif sort == "price_desc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat).order_by("-filter__price"), pag)
    elif sort == "asc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat).order_by("filter__article"), pag)
    elif sort == "desc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat).order_by("-filter__article"), pag)
    else:
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True, filter__category=cat), pag)

    try:
        filter_image_list = paginator.page(page_num)
    except InvalidPage:
        filter_image_list = paginator.page(1)

    return render(req, "filters_of_category.html", locals())


def brand_in_category(req, brand, cat):  # Выборка по брендам
    # Ддя боковых меню
    brands = Brand.objects.order_by("name")
    categorys = Category.objects.order_by("name")
    # *****************************************
    try:
        page_num = req.GET["page"]
    except KeyError:
        page_num = 1

    try:
        pag = req.GET["pag"]
        has_pag = True
    except MultiValueDictKeyError:
        has_pag = False
        pag = 20

    try:
        sort = req.GET["sort"]
        has_sort = True
    except MultiValueDictKeyError:
        sort = "default"
        has_sort = False

    br = Brand.objects.get(id_brand=brand)
    cat_id = Category.objects.get(id_category=cat)

    if sort == "price_asc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True, filter__category=cat_id,
                                       filter__brand=br).order_by("filter__price"), pag)
    elif sort == "price_desc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat_id, filter__brand=br).order_by("-filter__price"), pag)
    elif sort == "asc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat_id, filter__brand=br).order_by("filter__article"), pag)
    elif sort == "desc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat_id, filter__brand=br).order_by("-filter__article"), pag)
    else:
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True, filter__category=cat_id,
                                       filter__brand=br), pag)
    try:
        filter_image_list = paginator.page(page_num)
    except InvalidPage:
        filter_image_list = paginator.page(1)
    return render(req, "brand_in_category.html", locals())


def filter_of_brand(req, id):
    # Ддя боковых меню
    brands = Brand.objects.order_by("name")
    categorys = Category.objects.order_by("name")
    # *****************************************
    try:
        page_num = req.GET["page"]
    except KeyError:
        page_num = 1
    try:
        pag = req.GET["pag"]
        has_pag = True
    except MultiValueDictKeyError:
        has_pag = False
        pag = 20

    try:
        sort = req.GET["sort"]
        has_sort = True
    except MultiValueDictKeyError:
        sort = "default"
        has_sort = False

    br = Brand.objects.get(id_brand=id)
    if sort == "price_asc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True, filter__brand=br).order_by(
                "filter__price"), pag)
    elif sort == "price_desc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__brand=br).order_by("-filter__price"), pag)
    elif sort == "asc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__brand=br).order_by("filter__article"), pag)
    elif sort == "desc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__brand=br).order_by("-filter__article"), pag)
    else:
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True, filter__brand=br), pag)
    all_cat = Category.objects.all()
    try:
        filter_image_list = paginator.page(page_num)
    except InvalidPage:
        filter_image_list = paginator.page(1)
    return render(req, "filter_of_brand.html", locals())


def category_in_brand(req, brand, cat):
    # Ддя боковых меню
    brands = Brand.objects.order_by("name")
    categorys = Category.objects.order_by("name")
    # *****************************************
    try:
        page_num = req.GET["page"]
    except KeyError:
        page_num = 1
    try:
        pag = req.GET["pag"]
        has_pag = True
    except MultiValueDictKeyError:
        has_pag = False
        pag = 20

    try:
        sort = req.GET["sort"]
        has_sort = True
    except MultiValueDictKeyError:
        sort = "default"
        has_sort = False
    br = Brand.objects.get(id_brand=brand)
    cat_id = Category.objects.get(id_category=cat)
    if sort == "price_asc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True, filter__category=cat_id,
                                       filter__brand=br).order_by("filter__price"), pag)
    elif sort == "price_desc":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat_id, filter__brand=br).order_by("-filter__price"), pag)
    elif sort == "asc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat_id, filter__brand=br).order_by("filter__article"), pag)
    elif sort == "desc_article":
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True,
                                       filter__category=cat_id, filter__brand=br).order_by("-filter__article"), pag)
    else:
        paginator = Paginator(
            FilterImage.objects.filter(is_active=True, is_main=True, filter__is_active=True, filter__category=cat,
                                       filter__brand=br), pag)
    all_cat = Category.objects.all()
    try:
        filter_image_list = paginator.page(page_num)
    except InvalidPage:
        filter_image_list = paginator.page(1)
    return render(req, "category_in_brand.html", locals())


def filter_card(req, id):
    # Ддя боковых меню
    brands = Brand.objects.order_by("name")
    categorys = Category.objects.order_by("name")
    # *****************************************
    filter_item = Filter.objects.get(id_filter=id)
    if filter_item.discount > 0:
        price = filter_item.new_price
    else:
        price = filter_item.price

    cat = filter_item.category
    brand = filter_item.brand
    session_key = req.session.session_key
    if not session_key:
        req.session.cycle_key()
    print(req.session.session_key)
    return render(req, "filter_card.html", locals())
