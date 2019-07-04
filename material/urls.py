from django.contrib import admin
from django.urls import path,include
from material import views


app_name='material'
urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<int:meterid>/',views.delete,name='delete'),
    path('search/',views.search,name='search'),
    path('addtion/',views.addtion,name='addtion'),
    path('modifys/<int:meterid>',views.modifys,name='modifys'),
]