from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *
import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test # user_passes_test dùng để phân quyền
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def insert_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(" Tạo tài khoản thành công")
    form = UserForm()
    return render(request,'source/them_user.html',{'form':form})
