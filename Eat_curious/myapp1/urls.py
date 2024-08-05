from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
    path('recipes', views.recipes, name='recipes'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup_view, name='signup'),
    path('homes', views.homes, name='homes'),
    path('main', views.main, name='main'),
    path('users', views.users, name='users'),
    path('logout', views.logout_view, name='logout'),
]
