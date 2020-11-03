from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('tracking',views.tracking,name='tracking'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('single_product',views.single_product,name='single_product'),
]