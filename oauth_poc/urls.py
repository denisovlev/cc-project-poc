from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('authorize', views.authorize, name='authorize'),
    path('fetch_resource', views.fetch_resource, name='fetch_resource'),
]