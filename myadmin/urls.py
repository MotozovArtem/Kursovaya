from django.conf.urls import url
from myadmin import views
from .formclass import *

urlpatterns = [
    url(r'^$', views.myadmin, name='myadmin'),
    url(r'^filters/$', views.product, name='admin_filter'),
    url(r'^brands/$', views.brands, name='admin_brand'),
    url(r'^categories/$', views.categories, name='admin_cat'),
    url(r'^orders/$', views.orders, name='admin_order'),

    url(r"^filters/add$", FilterCreate.as_view(), name="add_filter"),
    url(r"^filters/edit/(?P<id>\d+)$", FilterEdit.as_view(), name="edit_filter"),
    url(r"^filters/del/$", views.filter_del, name="delete_filter"),

    url(r"^brands/add$", BrandCreate.as_view(), name="add_brand"),
    url(r"^brands/edit/(?P<id>\d+)$", BrandEdit.as_view(), name="edit_brand"),
    url(r"^brands/del/$", views.brand_del, name="delete_brand"),

    url(r"^categories/add$", CategoryCreate.as_view(), name="add_cat"),
    url(r"^categories/edit/(?P<id>\d+)$", CategoryEdit.as_view(), name="edit_cat"),
    url(r"^categories/del/$", views.cat_del, name="delete_cat"),

    url(r"^orders/add$", OrderCreate.as_view(), name="add_order"),
    url(r"^orders/edit/(?P<id>\d+)$", OrderEdit.as_view(), name="edit_order"),
    url(r"^orders/del/$", views.order_del, name="delete_order"),
    url(r"^orders/details/(?P<id>\d+)$", views.order_detail, name="detail_order"),
]
