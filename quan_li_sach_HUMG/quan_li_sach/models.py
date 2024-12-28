from django.db import models

# Create your models here.

class sach(models.Model):
    name = models.CharField(max_length=100)
    tac_gia = models.CharField(max_length=100)
    Nhom_hoc_phan = models.ForeignKey('Nhom_hoc_phan',on_delete=models.RESTRICT,null=True,blank=True)
    nam_xuat_ban = models.IntegerField(null=True)
    so_luong = models.IntegerField(null=True)
    def __str__(seft):
        return seft.name

class Loai_sach (models.Model):
    loai_sach = models.CharField(max_length=100)
    

    def __str__(seft):
        return seft.loai_sach

class Nhom_hoc_phan (models.Model):
    nhom_hoc_phan = models.CharField(max_length=100)
    Loai_sach = models.ForeignKey('Loai_sach',on_delete=models.RESTRICT,null=True,blank=True)
    def __str__(seft):
        return seft.nhom_hoc_phan

class account(models.Model):
    name_user = models.CharField(max_length=20)
    sdt = models.CharField()
    cccd = models.CharField()
    def __str__(seft):
        return seft.name_user 

class Muon_sach(models.Model):
    sach = models.ForeignKey('sach',on_delete=models.RESTRICT,null=True,blank=True)
    account = models.ForeignKey('account',on_delete=models.RESTRICT,null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    end_time = models.DateTimeField(null=True,blank=True)
    def __str__(seft):
        return seft.sach.loai_sach + ' - ' + seft.account.name

class Sach_account(models.Model):
    sach = models.ForeignKey('sach',on_delete=models.RESTRICT,null=True,blank=True)
    account = models.ForeignKey('account',on_delete=models.RESTRICT,null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    end_time = models.DateTimeField(null=True,blank=True)

    def __str__(seft):
        return seft.sach.name + " - " + seft.account.name_user