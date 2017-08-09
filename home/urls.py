#cs3773-group9/home/urls.py

#from django.conf.urls import url
#from home import views

#urlpatterns = [
#   url(r'^$', views.HomePageView.as_view(), name='index'), # URL has been named
#    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
#]
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'accountlogin.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
]