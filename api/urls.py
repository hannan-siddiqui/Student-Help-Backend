from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    
    path('student/', StudentView.as_view()),
    path('update/<pk>',DetailsUpdate.as_view()),
    path('delete/<pk>',DetailsDelete.as_view()),
    
    path('job/', JobView.as_view()),
    path('jobupdate/<pk>', JobUpdate.as_view() ),
    path('jobdelete/<pk>', JobDelete.as_view() ),
   
]