
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login'),
    path('signup', views.signup_page, name= 'signup'),
    path('home', views.home, name='home')
]
