from django.urls import path
from . import views

urlpatterns = [
    path ('insert_computer', views.insert_comuter,name="insert_computer"),

    path ('danh_sach', views.danh_sach,name="danh_sach"),

    path ('search_computer', views.search_computer,name="search_computer"),

    path ('insert_user', views.insert_user,name="insert_user"),

    path ('danh_sach_user', views.danh_sach_user,name="danh_sach_user"),

    path ('thiet_lap_cuoc_choi', views.thiet_lap_cuoc_choi,name="thiet_lap_cuoc_choi"),

    path ('view_computers_account', views.view_computers_account,name="view_computers_account"),

    path('stop-service/<int:id>/', views.stop_using_service, name='stop_using_service'),

    path('view_computers_account_historic', views.view_computers_account_historic, name='view_computers_account_historic'),

    path('login_view', views.login_view, name='login_view'),

    path('index', views.index, name='index'),

    path('logout_view', views.logout_view, name='logout_view'),


    


]