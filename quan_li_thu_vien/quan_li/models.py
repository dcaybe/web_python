from django.db import models

# Create your models here.
class muon_tra(models.Model):
    ma_muon_tra = models.IntegerField()
    ma_sach = models.CharField(max_length=100)
    ma_sv = models.IntegerField()
    ngay_muon = models.DateField()
    han_tra= models.DateField()
    ngay_tra = models.DateField()
    def __str__(self):
      return str(self.ma_muon_tra) + ' - ' + str(self.ma_sach) + ' - ' +str( self.ma_sv) + ' - ' + str(self.ngay_muon)+ ' - ' + str(self.han_tra) + ' - ' + str(self.ngay_tra) 
class sach(models.Model):
    ma_sach = models.IntegerField()
    ten_sach = models.CharField(max_length=100)
    vi_tri = models.CharField(max_length=100)
    def __str__(self):
        return str(self.ma_sach) + ' - ' + str(self.ten_sach) + ' - ' + str(self.vi_tri)
class sinh_vien(models.Model):
    ma_sv = models.IntegerField()
    ngay_muon = models.DateField()
    han_tra = models.DateField()
    def __str__(self):
        return str(self.ma_sv) + ' - ' + str(self.ngay_muon) + ' - ' + str(self.han_tra)
class nhan_vien(models.Model):
    ma_nv = models.IntegerField()
    ten_nv = models.CharField(max_length=100)
    def __str__(self):
        return str(self.ma_nv) + ' - ' + str(self.ten_nv)
class the_thu_vien(models.Model):
    ma_the = models.IntegerField()
    ma_sv = models.IntegerField()
    ngay_lap = models.DateField()
    def __str__(self):
        return str(self.ma_the) + ' - ' + str(self.ma_sv) + ' - ' + str(self.ngay_lap)
class nhap_sach(models.Model):
    ma_nhap = models.IntegerField()
    ma_sach = models.IntegerField()
    ma_nv = models.IntegerField()
    ngay_nhap = models.DateField()
    def __str__(self):
        return str(self.ma_nhap) + ' - ' + str(self.ma_sach) + ' - ' + str(self.ma_nv) + ' - ' + str(self.ngay_nhap)


