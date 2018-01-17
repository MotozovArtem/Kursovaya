from django.conf.urls import url
from filters import views

urlpatterns = [
    url(r'^top/$', views.top, name="top"),
    url(r'^category/(?:(?P<id>\d+)/)?$', views.filter_of_category, name="filter_of_category"),
    url(r'^brand/(?:(?P<id>\d+)/)?$', views.filter_of_brand, name="filter_of_brand"),
    url(r'^brand_in_category/(?P<brand>\d+)/(?P<cat>\d+)/$', views.brand_in_category, name="brand_in_category"),
    url(r'^category_in_brand/(?P<brand>\d+)/(?P<cat>\d+)/$', views.category_in_brand, name="category_in_brand"),
    url(r'^filter_card/(?P<id>\d+)/$', views.filter_card, name="filter_card"),

]
