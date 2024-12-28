from django.urls import path
from . import views

urlpatterns = [
    path ('insert_sinh_vien', views.insert_sinh_vien,name="insert_sinh_vien"),

    path ('insert_departments', views.insert_departments,name="insert_departments"),

    path ('insert_majors', views.insert_majors,name="insert_majors"),

    path ('home', views.home,name="home"),

    path ('change/<str:student_name>/<str:Majors_name>/<str:Departments_name>', views.change,name="change"),

    path ('delete/<str:student_name>', views.delete,name="delete"),

]