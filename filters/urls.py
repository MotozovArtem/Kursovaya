from django.conf.urls import url
from filters import views

urlpatterns = [
    url(r'^$', views.index, name="filters")
]