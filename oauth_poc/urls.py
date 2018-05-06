from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_raco, name='login'),
    path('authorize', views.authorize, name='authorize'),
    path('fetch_resource', views.fetch_resource, name='fetch_resource'),
    path('register', views.register, name='register'),
]