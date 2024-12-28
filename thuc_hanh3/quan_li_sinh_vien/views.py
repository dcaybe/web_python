from django.shortcuts import render,redirect        
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def insert_sinh_vien(request):
    if request.method == 'POST':
        form = Insert_Major_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them moi may tinh thanh cong")
    form = Insert_Major_form()
    return render(request,'source/nhap_sinh_vien.html',{'form':form})

def insert_majors(request):
    if request.method == 'POST':
        form = Insert_Departments_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them moi may tinh thanh cong")
    form = Insert_Departments_form()
    return render(request,'source/nhap_major.html',{'form':form})


def insert_departments(request):
    if request.method=='POST':
        Departments_name=request.POST.get('Departments_name')
        Departments.objects.create(Departments_name = Departments_name)
        return HttpResponse("Thêm mới departments thành công")
    return render(request,"source/nhap_departments.html")

def home(request):
    sinhviens = sinh_vien.objects.all()
    return render(request,"source/hien_thi_sv.html",{'sinhviens':sinhviens})

def change(request,student_name,Majors_name,Departments_name):
    if request.method=='POST':
        student_name_new=request.POST.get('student_name_new')
        gioi_tinh_new=request.POST.get('gioi_tinh_new')
        birthday_new=request.POST.get('birthday_new')
        Majors_name_new=request.POST.get('Majors_name_new')
        Departments_name_new=request.POST.get('Departments_name_new')
        sinh_vien.objects.filter(student_name = student_name).update(student_name = student_name_new,gioi_tinh = gioi_tinh_new,birthday = birthday_new)
        Departments.objects.filter(Departments_name = Departments_name).update(Departments_name = Departments_name_new)
        Majors.objects.filter(Majors_name = Majors_name).update(Majors_name = Majors_name_new)
        return HttpResponse("Thay đổi thông tin thành công")
    return render(request,"source/change.html")

def delete(request,student_name): 
    sinh_vien.objects.filter(student_name=student_name).delete()
    return redirect("home")

# def change_sinh_vien(request,student_name_old):
#     if request.method=='POST':
#         student_name_new=request.POST.get('student_name_new')
#         gioi_tinh_new=request.POST.get('gioi_tinh_new')
#         birthday_new=request.POST.get('birthday_new')
#         Departments.objects.filter(student_name = student_name_old).update(student_name = student_name_new,gioi_tinh = gioi_tinh_new,birthday = birthday_new)
#         return HttpResponse("Thay đổi thông tin sinh viên thành công")
#     return render(request,"source/change_sinh_vien.html")

# def change_majors(request,Major):
#     if request.method=='POST':
#         Departments_name=request.POST.get('Departments_name')
#         Departments.objects.create(Departments_name = Departments_name)
#         return HttpResponse("Thêm mới departments thành công")
#     return render(request,"source/change_majors.html")