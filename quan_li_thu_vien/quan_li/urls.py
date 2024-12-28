from django.urls import path
from . import views 


urlpatterns = [
    path('abc', views.index,name="index"),
    path('hello/<str:name>', views.hello,name="hello"),
    path('third', views.third,name="third"),
    path('tao_moi_sach', views.tao_moi_sach,name="tao_moi_sach"), 
    path('tao_moi_sach1/<int:ma_sach>/<str:ten_sach>/<str:vi_tri>', views.tao_moi_sach1,name="tao_moi_sach"), 
    path('xem_sach', views.xem_sach,name="xem_sach"),
    path('xoa_sach', views.xoa_sach,name="xoa_sach"),
    path('cap_nhat_sach/<str:ten_sach>/<str:ten_sach_moi>', views.cap_nhat_sach,name=" cap_nhat_sach"),
    path('hienthihtml',views.hienthihtml,name="hienthihtml"),
    # nhan_vien
    path('themnhanvien/<str:ten>/<int:ma>',views.themnhanvien,name="themnhanvien"),
    path('suathongtin/<str:tencu>/<str:tenmoi>',views.suathongtin,name="suathongtin"),
    
    path('xemnhanvien',views.xemnhanvien,name="xemnhanvien"),
    # the_thu_vien
    path('themthe/<int:ma_the>/<int:ma_sv>/<str:ngay_lap>',views.themthe,name="themthe"),
    path('sua_the/<int:ma_the>/<int:ma_sv_moi>',views.sua_the,name="sua_the"),
    path('xoa_the/<int:ma_the>',views.xoa_the,name="xoa_the"),
    path('xemthe',views.xemthe,name="xemthe"),
    # nhap_sach
    path('themnhapsach/<int:ma_nhap>/<int:ma_sach>/<int:ma_nv>/<str:ngay_nhap>',views.themnhapsach,name="themnhapsach"),
    path('suanhapsach/<int:ma_nhap>/<int:ma_sach_moi>',views.suanhapsach,name="suanhapsach"),
    path('xoanhapsach/<int:ma_nhap>',views.xoanhapsach,name="xoanhapsach"),
    path('xemnhapsach',views.xemnhapsach,name="xemnhapsach"),

    path('cap_nhat_sach_html',views.cap_nhat_sach_html,name="cap_nhat_sach_html"),
    path('them_nhap_sach',views.them_nhap_sach,name="them_nhap_sach"),
    
    path('xem_nhap_sach_html',views.xem_nhap_sach_html,name="xem_nhap_sach_html"),
    
    path('hienthisachhtml/',views.hienthisachhtml,name="hienthisachhtml"),
    #sach
    path('suasachhtml/<int:ma_sach>/',views.suasachhtml,name="suasachhtml"),

    path('xoasachhtml/<int:ma_sach>/',views.xoasachhtml,name="xoasachhtml"),

    path('themsachhtml',views.themsachhtml,name="themsachhtml"),

    path('home',views.home,name="home"),
    
    #nhanvien
    path('nhanvien',views.nhanvien,name="nhanvien"),

    path('themnhanvien',views.themnhanvien,name="themnhanvien"),

    path('suanhanvien/<int:ma_nv>/',views.suanhanvien,name="suanhanvien"),

    path('xoanhanvien/<int:ma_nv>/',views.xoanhanvien,name="xoanhanvien"),
    
    #sinhvien
    path('sinhvien',views.sinhvien,name="sinhvien"),

    path('themsinhvien',views.themsinhvien,name="themsinhvien"),

    path('suasinhvien/<int:ma_sv>/',views.suasinhvien,name="suasinhvien"),

    path('xoasinhvien/<int:ma_sv>/',views.xoasinhvien,name="xoasinhvien"),

   

]