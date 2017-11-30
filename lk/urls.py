from django.conf.urls import url
from lk import views


urlpatterns = [
    url(r'^$', views.lichn_kab, name="lk"),

]