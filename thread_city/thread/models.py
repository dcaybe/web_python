from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.CharField()
#     password = models.CharField(max_length=128)  
#     def __str__(seft):
#         return seft.username

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.RESTRICT,null=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(seft):
        return seft.content
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.RESTRICT,null=True,blank=True)
    post = models.ForeignKey('Post',on_delete=models.RESTRICT,null=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(seft):
        return seft.content
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.RESTRICT,null=True,blank=True)
    post = models.ForeignKey('Post',on_delete=models.RESTRICT,null=True,blank=True)
    comment = models.ForeignKey('Comment',on_delete=models.RESTRICT,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    following = models.ForeignKey(User,on_delete=models.RESTRICT,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)