from django.db import models

# Create your models here.

class sinh_vien(models.Model):
    student_name = models.CharField(max_length=100)
    gioi_tinh = models.CharField(max_length=100,null=True) 
    birthday = models.DateField()
    Majors = models.ForeignKey('Majors',on_delete=models.RESTRICT,null=True,blank=True)
    def __str__(seft):
        return seft.student_name
    
class Majors(models.Model):
    Majors_name = models.CharField(max_length=100)
    Departments = models.ForeignKey('Departments',on_delete=models.RESTRICT,null=True,blank=True)
    def __str__(seft):
        return seft.Majors_name

class Departments(models.Model):
    Departments_name = models.CharField(max_length=100)
    def __str__(seft):
        return seft.Departments_name
                                                                                                    
