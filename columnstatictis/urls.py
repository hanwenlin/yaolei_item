from django.contrib import admin
from django.urls import path,include
from columnstatictis import views


app_name='columnstatictis'
urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<int:column_id>/',views.delete,name='delete'),
    path('search/',views.search,name='search'),
    path('addtion/',views.addtion,name='addtion'),
    path('modifys/<int:column_id>',views.modifys,name='modifys'),
]