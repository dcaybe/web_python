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

def insert_comuter(request):
    if request.method == 'POST':
        form = Insert_computer_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them moi may tinh thanh cong")
    form = Insert_computer_form()
    return render(request,'source/insert_computer.html',{'form':form})

def danh_sach(request):
    computers=Computer.objects.all() 
    return render(request,'source/danh_sach_mt.html',{'computers':computers})

# tìm kiếm
# def search_computer(request):
#     #lấy dữ liệu từ form
#     form = Computer_search_computer(request.GET or None)
#     # tạo biến computer trong trường hợp không tìm thấy biến phù hợp
#     computers = None

#     #kiểm tra thông tin người dùng khi đã chọn loại máy
#     if form.is_valid():
#         #lấy thông tin từ form
#         computer_type = form.cleaned_data.get('computer_type')
#         if computer_type:
#             #chạy lệnh đọc dữ liệu với điều kiện filter
#             computers=Computer.objects.filter(computer_type = computer_type)

#     return render(request,'source/search_computer.html',{'form':form,'computers':computers})

def search_computer(request):
    #lấy dữ liệu từ form
    form = Computer_search_computer(request.GET or None)
    # tạo biến computer trong trường hợp không tìm thấy biến phù hợp
    computers = None

    #kiểm tra thông tin người dùng khi đã chọn loại máy
    if form.is_valid():
        #lấy thông tin từ form
        computer_name = form.cleaned_data.get('computer_name')
        if computer_name:
            #chạy lệnh đọc dữ liệu với điều kiện filter
            computers=Computer.objects.filter(computer_name = computer_name)

    return render(request,'source/search_computer.html',{'form':form,'computers':computers})

def danh_sach_user(request):
    accounts=account.objects.all() 
    return render(request,'source/danh_sach_user.html',{'accounts':accounts})
@login_required
def insert_user(request):
    if request.method == 'POST':
        form = Insert_user_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Them khach thanh cong")
    form = Insert_user_form()
    return render(request,'source/them_khach.html',{'form':form})

def thiet_lap_cuoc_choi(request):
    if request.method == 'POST':
        form = Thiet_lap_cuoc_choi_form(request.POST)
        if form.is_valid():
            form.save()
            # thay đổi trạng thái của máy tính được lựa chọn
            form.instance.computer.trang_thai = 'Đang chơi'
            form.instance.computer.save()
            return HttpResponse("Thiết lập cuộc chơi thành công")
    form =Thiet_lap_cuoc_choi_form()
    return render(request, 'source/thiet_lap_cuoc_choi.html', {'form': form})

def view_computers_account(request):
# lọc các dữ liệu trong bảng computer_account chưa có end_time > vẫn đang sử dụng Computer_account.objects.all().filter(end_time_isnull=True)
    computer_accounts = Computer_account.objects.all().filter(end_time__isnull = True)
    return render(request, 'source/view_computers_account.html', {'computer_accounts': computer_accounts})


def view_computers_account_historic(request):
    computer_accounts = Computer_account.objects.all()
    return render(request, 'source/view_computers_account_historicko.html', {'computer_accounts': computer_accounts})

def stop_using_service (request, id):
    # tham chiếu đến đối tượng computer_account theo id
    computer_account = Computer_account.objects.get(id=id)
    computer_account.end_time = datetime.datetime.now() # lấy thời gian hiện tại
    computer_account.save()
    # thay đổi trạng thái của máy tính
    computer_account.computer.trang_thai = 'Đang trống'
    computer_account.computer.save()
    return HttpResponse ("Dừng sử dụng dịch vụ thành công")

def login_view(request):
    if request.method == "POST": # kjeerm tra xem form đã được gửi chưa
        username = request.POST.get('username')
        password = request.POST.get('password')
        # kiểm tra xem có tên người dùng không
        if not User.objects.filter(username=username).exists():
            return redirect('login_view')
        # kiểm tra xem tên người dùng và mật khẩu có đúng không
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Sai tài khoản')
            # người dùng không xác định được (sai mật khẩu)
            return redirect('login_view')
        else:
            # đăng nhập và điều hướng
            login(request, user)
            # điều hướng theo nhóm của người dùng
            return redirect('index')
        
    # render the login page template
    return render(request, 'source/login.html')

def index(request):
    return render(request,'source/index.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')