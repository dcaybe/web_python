from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    sachs = sach.objects.all()
    return render(request,"source/hien_thi_sach.html",{'sachs':sachs})

def delete(request,name):
    sach.objects.filter(name=name).delete()
    return redirect("home")

def insert_sach(request):
    if request.method == 'POST':
        form = Insert_sach_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them moi sach thanh cong")
    form = Insert_sach_form()
    return render(request, 'source/nhap_sach.html', {'form': form})

def insert_loai_sach(request):
    if request.method == 'POST':
        form = Insert_loai_sach_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them moi loai sach thanh cong")
    form = Insert_loai_sach_form()
    return render(request,'source/nhap_loai_sach.html',{'form':form})
def insert_nhom_hoc_phan(request):
    if request.method == 'POST':
        form = Insert_nhom_hoc_phan_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them moi nhom hoc phan thanh cong")
    form = Insert_nhom_hoc_phan_form()

    return render(request,'source/nhap_nhom_hoc_phan.html',{'form':form})

def danh_sach_user(request):
    accounts=account.objects.all() 
    return render(request,'source/danh_sach_user.html',{'accounts':accounts})

def insert_user(request):
    if request.method == 'POST':
        form = Insert_user_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them khach thanh cong")
    form = Insert_user_form()
    return render(request,'source/them_khach.html',{'form':form})

def thiet_lap_muon_sach(request):
    if request.method == 'POST':
        form = Thiet_lap_muon_sach_form(request.POST)
        if form.is_valid():
            form.save()
            # thay đổi trạng thái của máy tính được lựa chọn
            if(form.instance.sach.so_luong != 0):
                form.instance.sach.so_luong -= 1
            form.instance.sach.save()
            return HttpResponse("Thiết lập cuộc chơi thành công")
        else:
            return HttpResponse("Hết sách")
    form =Thiet_lap_muon_sach_form()
    return render(request, 'source/thiet_lap_muon_sach.html', {'form': form})

def view_Sach_account(request):
# lọc các dữ liệu trong bảng computer_account chưa có end_time > vẫn đang sử dụng Computer_account.objects.all().filter(end_time_isnull=True)
    Sach_accounts = Sach_account.objects.all().filter(end_time__isnull = True)
    return render(request, 'source/view_Sach_account.html', {'Sach_accounts': Sach_accounts})


def stop_using_service (request, id):
    # tham chiếu đến đối tượng computer_account theo id
    computer_account = Sach_account.objects.get(id=id)
    computer_account.end_time = datetime.datetime.now() # lấy thời gian hiện tại
    computer_account.save()
    # thay đổi trạng thái của máy tính
    computer_account.sach.so_luong +=1 
    computer_account.sach.save()
    return HttpResponse ("Dừng sử dụng dịch vụ thành công")

def view_Sach_account_historic(request):
    Sach_accounts = Sach_account.objects.all()
    return render(request, 'source/view_Sach_account_historic.html', {'Sach_accounts': Sach_accounts})

# def login_view(request):
#     if request.method == "POST":
#         username = request.POSt.get('username')
#         password = request.POSt.get('password')
#         # kiểm tra xen có tên người dùng không
#         if not User.objects.fillter(username=username).exists():
#             return redirect('login')
#         # kiểm tra xem tên ng dùng và password có đúng không
#         user = authenticate (username = username,password = password)
#         if user is None:
#             # người dùng không xác định được(sai password)
#             return redirect('login')
#         else:
#             #đăng nhập và điều hướng
#             login(request,user)
#             # điều hướng theo nhóm của người dùng
#             return redirect('view_computer_account')
        
#     # render the login page template
#     return render(request,'account/login.html')

