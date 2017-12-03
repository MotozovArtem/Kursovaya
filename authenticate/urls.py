from django.conf.urls import url
from authenticate import views

from authenticate.generic import UserCreate

urlpatterns = [
    url(r"^$", UserCreate.as_view(), name="auth"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
]
