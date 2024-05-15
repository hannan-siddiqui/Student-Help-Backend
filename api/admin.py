from django.contrib import admin
from .models import *

# Register your models here.


# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno', 'enrlno', 'course', 'phone', 'email', 'linkedin', 'github', 'desc', 'skills', 'image' )
   
    

admin.site.register(Student, StudentAdmin)