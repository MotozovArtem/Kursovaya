from django.conf.urls import url
from main import views
from main.views import *
urlpatterns = [
    url(r'^$', MainPageView.as_view(), name="main"),
]