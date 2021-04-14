from django.contrib import admin
from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('student_dashboard',views.student_view,name="student_view"),
    path('Detail',views.student_detail, name="student_detail"),
    path('Timetable',views.timetable,name="timetable")
    
]