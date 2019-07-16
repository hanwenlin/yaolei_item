from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import LoginForm,RegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
           # return HttpResponse('successfully')
            return redirect(reverse('index:index',args=()))
        else:
            return HttpResponse('sorry,you can not register')
    else:
        user_form = RegistrationForm()
        return render(request,'account/register.html',{'form':user_form})


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            print(user)
            if user:
                login(request,user)
                # return HttpResponse('登录成功')
                return render(request,'index/index.html')
            else:
                return HttpResponse('没有登录')
        else:
            return HttpResponse('Invalid login')
    else:
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})


def user_logout(request):
    logout(request)
    return render(request,'index/index.html')


def resetpwd(request):
    pass


