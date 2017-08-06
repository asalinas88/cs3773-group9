#cs3773-group9/home/urls.py

from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]