from django.shortcuts import render,redirect        
from django.http import HttpResponse
from .models import *
from .forms import *



def home(request):
    nhanviens = nhan_vien.objects.all()
    return render(request,"source/hien_thi_nv.html",{'nhanviens':nhanviens})

def delete(request,name):
    nhan_vien.objects.filter(name=name).delete()
    return redirect("home")

def insert_nhan_vien(request):
    if request.method == 'POST':
        form = Insert_nhan_vien_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them moi nhân viên thanh cong")
    form = Insert_nhan_vien_form()

    return render(request,'source/nhap_nhan_vien.html',{'form':form})

def search_nv(request):
    #lấy dữ liệu từ form
    form = nv_search(request.GET or None)
    # tạo biến computer trong trường hợp không tìm thấy biến phù hợp
    nhanviens = None

    #kiểm tra thông tin người dùng khi đã chọn loại máy
    if form.is_valid():
        #lấy thông tin từ form
        vi_tri = form.cleaned_data.get('vi_tri')
        if vi_tri:
            #chạy lệnh đọc dữ liệu với điều kiện filter
            nhanviens=nhan_vien.objects.filter(vi_tri = vi_tri)

    return render(request,'source/search_nv.html',{'form':form,'nhanviens':nhanviens})