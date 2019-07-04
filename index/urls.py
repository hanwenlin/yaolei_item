from django.contrib import admin
from django.urls import path,include
from index import views


app_name = 'index'
urlpatterns = [
    path('', views.index,name='index'),
]