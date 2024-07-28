from django.contrib import admin
from .models import *

# Register your models here.


# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno', 'enrlno', 'course', 'phone', 'email', 'linkedin', 'github', 'desc', 'skills', 'image' )

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'desc', 'link']
    

admin.site.register(Student, StudentAdmin)
admin.site.register(Job, JobAdmin)
