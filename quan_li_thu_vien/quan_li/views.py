from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request): 
    return HttpResponse('My first Django')
def hello(request,name): 
    return HttpResponse(f"hello{name}")
def third(request): 
    return HttpResponse('<b>Xin chúc mùng bạn đã tạo môt view mới<b>')
def tao_moi_sach(request):
    sach.objects.create(ma_sach='10',ten_sach='python',vi_tri='98')
    return HttpResponse("da them sach moi")
def tao_moi_sach1(request,ma_sach,ten_sach,vi_tri):
    sach.objects.create(ma_sach=ma_sach,ten_sach=ten_sach,vi_tri=vi_tri)
    return HttpResponse("da them sach moi {ten_sach}")
def xem_sach(request):   
    return HttpResponse(sach.objects.all())
def xoa_sach(request,sach1):
    sach.objects.filter(ten_sach=sach1).delete()
    return HttpResponse('da xoa sach')
def cap_nhat_sach(request,ten_sach,ten_sach_moi):
    sach.objects.filter(ten_sach=ten_sach).update(ten_sach=ten_sach_moi)
    return HttpResponse('da cap nhat sach')
def hienthihtml(request):
    return render(request,'bai7_web_humg.html')
# nhan_vien
def themnhanvien(request,ten,ma):
    nhan_vien.objects.create(ten_nv=ten,ma_nv=ma)
    return HttpResponse("da them nhan vien")
def suathongtin(request,tencu,tenmoi):
    nhan_vien.objects.filter(ten_nv=tencu).update(ten_nv=tenmoi)
    return HttpResponse('da cap nhat nhan vien')

def xemnhanvien(request):
    return HttpResponse(nhan_vien.objects.all())
# the_thu_vien
def themthe(request,ma_the,ma_sv,ngay_lap):
    the_thu_vien.objects.create(ma_the=ma_the,ma_sv=ma_sv,ngay_lap=ngay_lap)
    return HttpResponse("da them the")
def sua_the(request,ma_the,ma_sv_moi):
    the_thu_vien.objects.filter(ma_the=ma_the).update(ma_sv=ma_sv_moi)
    return HttpResponse('da cap nhat the')
def xoa_the(request,ma_the):
    the_thu_vien.objects.filter(ma_the=ma_the).delete()
    return HttpResponse('da xoa the')
def xemthe(request):
    return HttpResponse(the_thu_vien.objects.all())
#nhap_sach
def themnhapsach(request,ma_nhap,ma_sach,ma_nv,ngay_nhap):
    nhap_sach.objects.create(ma_nhap=ma_nhap,ma_sach=ma_sach,ma_nv=ma_nv,ngay_nhap=ngay_nhap)
    return HttpResponse("da them nhap sach")
def suanhapsach(request,ma_nhap,ma_sach_moi):
    nhap_sach.objects.filter(ma_nhap=ma_nhap).update(ma_sach=ma_sach_moi)
    return HttpResponse('da cap nhat nhap sach')
def xoanhapsach(request,ma_nhap):
    nhap_sach.objects.filter(ma_nhap=ma_nhap).delete()
    return HttpResponse('da xoa nhap sach')
def xemnhapsach(request):
    return redirect("hienthisachhtml")
def cap_nhat_sach_html(request):
    if request.method=='POST':
        ma_sach=request.POST.get('ma_sach')
        ma_nhap_moi=request.POST.get('ma_nhap')
        nhap_sach.objects.filter(ma_sach=ma_sach).update(ma_nhap=ma_nhap_moi)
        return HttpResponse("da cap nhat ma nhap")
    return render(request,"nhap_sach.html")
def them_nhap_sach(request):
    if request.method=='POST':
        ma_sach=request.POST.get('ma_sach')
        ma_nhap=request.POST.get('ma_nhap')
        ma_nv=request.POST.get('ma_nv')
        ngay_nhap=request.POST.get('ngay_nhap')
        nhap_sach.objects.create(ma_nhap=ma_nhap,ma_sach=ma_sach,ma_nv=ma_nv,ngay_nhap=ngay_nhap)
        return HttpResponse("da cap nhat ma nhap")
    return render(request,"source/nhap_sach.html")

def xem_nhap_sach_html(request):
    nhap_sach.objects.all()
    return render(request,"source/hienthinhapsach",{'nhap_sach':nhap_sach})

def hienthisachhtml(request):
    sachs = sach.objects.all().order_by('ma_sach') 
    return render(request,"source/hienthisach.html",{'sachs':sachs})
#sach
def home(request):
    sachs = sach.objects.all().order_by('ma_sach') 
    return render(request,"source/home.html",{'sachs':sachs})

def suasachhtml(request,ma_sach):
    if request.method=='POST':

        ten_sach=request.POST.get('ten_sach')
        
        sach.objects.filter(ma_sach=ma_sach).update( ten_sach= ten_sach)
        return redirect('home')
    return render(request,"source/suasach.html")

def xoasachhtml(request,ma_sach):
    sach.objects.filter(ma_sach=ma_sach).delete()
    return redirect("home")

def themsachhtml(request):
    if request.method=='POST':
        ma_sach=request.POST.get('ma_sach')
        ten_sach=request.POST.get('ten_sach')
        vi_tri=request.POST.get('vi_tri')
        sach.objects.create(ma_sach=ma_sach,ten_sach=ten_sach,vi_tri=vi_tri)
        return redirect('home')
    return render(request,"source/themsach.html")

#nhanvien
def nhanvien(request):
    nhanviens = nhan_vien.objects.all().order_by('ma_nv') 
    return render(request,"source/nhanvien.html",{'nhanviens':nhanviens})

def themnhanvien(request):
    if request.method=='POST':
        ma_nv=request.POST.get('ma_nv')
        ten_nv=request.POST.get('ten_nv')
        nhan_vien.objects.create( ma_nv= ma_nv,ten_nv=ten_nv)   
        return redirect('nhanvien')
    return render(request,"source/themnhanvien.html")

def suanhanvien(request,ma_nv):
    if request.method=='POST':

        ten_nv=request.POST.get('ten_nv')
        
        sach.objects.filter(ma_nv=ma_nv).update( ten_nv= ten_nv)
        return redirect('nhanvien')
    return render(request,"source/suanhanvien.html")

def xoanhanvien(request,ma_nv):
    nhan_vien.objects.filter(ma_nv=ma_nv).delete()
    return redirect("nhanvien")

#sinhvien
def sinhvien(request):
    sinhviens = sinh_vien.objects.all().order_by('ma_sv') 
    return render(request,"source/sinhvien.html",{'sinhviens': sinhviens})

def themsinhvien(request):
    if request.method=='POST':
        ma_sv=request.POST.get('ma_sv')
        ngay_muon=request.POST.get('ngay_muon')
        han_tra=request.POST.get('han_tra')
        sinh_vien.objects.create( ma_sv=ma_sv,ngay_muon=ngay_muon,han_tra=han_tra)   
        return redirect('sinhvien')
    return render(request,"source/themsinhvien.html")

def suasinhvien(request,ma_sv):
    if request.method=='POST':

        ma_sv=request.POST.get('ma_sv')
        ngay_muon=request.POST.get('ngay_muon')
        han_tra=request.POST.get('han_tra')
        sinh_vien.objects.filter(ma_sv=ma_sv).update( ma_sv=ma_sv,ngay_muon=ngay_muon, han_tra= han_tra)
        return redirect('sinhvien')
    return render(request,"source/suasinhvien.html")

def xoasinhvien(request,ma_sv):
    sinh_vien.objects.filter(ma_sv=ma_sv).delete()
    return redirect("sinhvien")

