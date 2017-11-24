from django.conf.urls import url
from brands import views

urlpatterns = [
    url(r'^$', views.index, name="brands")
]