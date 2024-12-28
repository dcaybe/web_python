from django.urls import path
from . import views

urlpatterns = [
    path ('insert_sach', views.insert_sach,name="insert_sach"),

    path ('insert_loai_sach', views.insert_loai_sach,name="insert_loai_sach"),

    path ('insert_nhom_hoc_phan', views.insert_nhom_hoc_phan,name="insert_nhom_hoc_phan"),


    path ('insert_user', views.insert_user,name="insert_user"),

    path ('home', views.home,name="home"),

    path ('view_Sach_account', views.view_Sach_account,name="view_Sach_account"),

    path ('thiet_lap_muon_sach', views.thiet_lap_muon_sach,name="thiet_lap_muon_sach"),

    path ('delete/<str:name>', views.delete,name="delete"),

    path ('stop_using_service/<int:id>', views.stop_using_service,name="stop_using_service"),

    path ('view_Sach_account_historic', views.view_Sach_account_historic,name="view_Sach_account_historic"),



]