from django.urls import path
from . import views

urlpatterns = [
    path ('insert_nhan_vien', views.insert_nhan_vien,name="insert_nhan_vien"),

  
    path ('home', views.home,name="home"),

    path ('delete/<str:name>', views.delete,name="delete"),

    path ('search_nv', views.search_nv,name="search_nv")




]