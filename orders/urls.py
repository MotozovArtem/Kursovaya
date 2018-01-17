from django.conf.urls import url
from orders import views

urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name="basket_adding"),
    url(r"^basket_update/$", views.basket_update, name="basket_update"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^order_create/$', views.PrepareOrder.as_view(), name="prepare_order"),
]
