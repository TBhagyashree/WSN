from django.contrib import admin
from django.urls import path

from . import views

app_name = 'attendence'

urlpatterns = [
    path('attendence_save/',views.attendence_save,name="attendence"),
    path('dafaulters/',views.defaulters,name="defaulters"),
    path('attendence_student/',views.attendence_student,name="attendence_student")
]