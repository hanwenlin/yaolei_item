from django.contrib import admin
from django.urls import path,include
from termlist import views


app_name='termlist'
urlpatterns = [
    path('', views.index,name='index'),
    path('search/',views.search,name='search'),
    path('addtion/',views.addtion,name='addtion'),
    path('modifys/<int:productid>',views.modifys,name='modifys'),
]