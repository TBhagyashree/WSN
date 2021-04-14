
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'Teacher'

urlpatterns = [
    path('Teacher_div_selection/',views.Teacher_view,name="Teacher_view"),
    path('Time_table/',views.Time_table,name="Time_table"),
    path('Teacher_dashboard/',views.Teacher_view_dashboard,name="Teacher_view_dashboard"),
    path('Students/',views.students,name="students"),
    path('Email/',views.email, name='Email'),
    path('Time_table_delete/',views.Time_table_delete,name="Time_table_delete"),
    path('calculate/',views.Calculate_attendence,name="calculate"),
    

]