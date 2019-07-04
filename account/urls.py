from django.contrib import admin
from django.urls import path,include
from account import views


app_name='account'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('resetpwd/',views.resetpwd,name='resetpwd'),
]

# 用户名 yaolei  密码 yaolei1353516732