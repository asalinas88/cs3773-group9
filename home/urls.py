#cs3773-group9/home/urls.py

from django.conf.urls import url
from django.contrib.auth.views import login
from home import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'), # URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^login/$', login, {'template_name': 'login.html'}),
]