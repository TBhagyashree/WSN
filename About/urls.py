from django.contrib import admin
from django.urls import path

from . import views

app_name = 'About'

urlpatterns = [
    path('teacher',views.About_view_teacher,name="About_view_teacher"),
    path('student',views.About_view_student,name="About_view_student"),
    
]