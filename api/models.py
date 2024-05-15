from django.db import models


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



class Student(models.Model):

    name = models.TextField(max_length=30, null=True)
    rollno = models.TextField(max_length = 30, null=True)
    enrlno = models.TextField(max_length=20,null=True)
    course = models.TextField(max_length=30, default='MCA', null=True)
    phone = models.TextField(max_length=15, null=True) 
    email = models.TextField(max_length=50, unique=True)
    linkedin = models.TextField(max_length=100, null=True)
    github = models.TextField(max_length=100, null=True)
    desc = models.TextField(max_length=500, null= True)
    skills = models.TextField(max_length = 500, null=True)
    image = models.ImageField(upload_to='photo/', null=True, )
