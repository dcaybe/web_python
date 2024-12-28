from django.db import models

# Create your models here.

class nhan_vien(models.Model):
    name = models.CharField(max_length=100)
    vi_tri = models.ForeignKey('Vi_tri',on_delete=models.RESTRICT,null=True,blank=True)
    tuoi = models.IntegerField()
    gioi_tinh = models.CharField()
    mode = models.ForeignKey('Mode',on_delete=models.RESTRICT,null=True,blank=True)
    def __str__(seft):
        return seft.name

class Vi_tri (models.Model):
    vi_tri_lam = models.CharField(max_length=100)
    def __str__(seft):  
        return seft.vi_tri_lam

class Mode (models.Model):
    Mode_lam = models.CharField(max_length=100)
    def __str__(seft):
        return seft.Mode_lam

