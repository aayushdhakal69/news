from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.blogHome, name= "blogHome"),
    path('<str:slug>', views.blogPost, name= "blogPost"),
    path('search/', views.search, name="search")
]