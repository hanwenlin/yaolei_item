from django.contrib import admin
from django.urls import path,include
from issues import views

app_name='issues'
urlpatterns = [
    path('', views.index,name='index'),
    path('search/',views.search,name='search'),
    path('addtion/',views.addtion,name='addtion'),
    path('modifys/<int:issueid>',views.modifys,name='modifys'),
    path('issue_meterial/addition/',views.issuemeterial_addtion,name='issuemeterial_addtion'),
    path('issue_meterial/modifys/<int:issuemeterid>',views.issuemeterial_modify,name='issuemeterial_modify'),
    path('issue_meterial/search/',views.issuemeterial_search,name='issuemeterial_search'),
]