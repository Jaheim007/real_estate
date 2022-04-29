from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.index2, name='index2'),
    path('signup', views.index3, name= 'index3')
]
