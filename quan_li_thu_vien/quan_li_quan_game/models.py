from django.db import models

# Create your models here.

class Computer(models.Model):
    computer_name = models.CharField(max_length=255)
    computer_type = models.ForeignKey('Computer_type',on_delete=models.RESTRICT,null=True,blank=True)
    trang_thai = models.CharField(max_length=20,null=True,blank=True)

    def __str__(seft):
        return seft.computer_name
    
class Computer_type(models.Model):
    computer_type_name = models.CharField(max_length=20)
    configuration = models.TextField()
    price = models.FloatField()
    def __str__(seft):
        return seft.computer_type_name 

class account(models.Model):
    name_user = models.CharField(max_length=20)
    password = models.CharField()
    balance = models.FloatField()
    def __str__(seft):
        return seft.name_user 

class Computer_account(models.Model):
    computer = models.ForeignKey('Computer',on_delete=models.RESTRICT,null=True,blank=True)
    account = models.ForeignKey('account',on_delete=models.RESTRICT,null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    end_time = models.DateTimeField(null=True,blank=True)

    def __str__(seft):
        return seft.computer.computer_name + " - " + seft.account.account_name