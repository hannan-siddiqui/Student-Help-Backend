from django.db import models


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



class Student(models.Model):

# personal info
    name = models.TextField(max_length=30, null=True)
    rollno = models.TextField(max_length = 30, null=True)
    enrlno = models.TextField(max_length=20,null=True)
    course = models.TextField(max_length=30, default='MCA')
    phone = models.TextField(max_length=15, null=True) 
    email = models.TextField(max_length=50, unique=True)

# social links

    link = models.TextField(max_length=100, null=True)
    linkedin = models.TextField(max_length=100, null=True)
    github = models.TextField(max_length=100, null=True)
    twitter = models.TextField(max_length=100, null=True)

# portfolio info
    desc = models.TextField(max_length=500, null= True)
    skills = models.TextField(max_length = 500, null=True)
    image = models.ImageField(upload_to='photo/', null=True)

# project
    projects = models.JSONField(null=True)

# leetcode
    leetcode = models.JSONField(null=True)



class Job(models.Model):
    title = models.TextField(null=True)
    company = models.TextField(null=True)

    # remote and worktype
    remote = models.TextField(null=True)
    worktype = models.TextField(null=True)
    location = models.TextField(null=True)

    # about the job
    desc = models.TextField(null=True)
    # qualification
    qualification = models.TextField(null=True)

    
    link = models.TextField(null=True)


    


