from django.contrib import admin
from django.urls import path

from . import views

app_name = 'Authenticate'

urlpatterns = [

    #path('signup',views.signup_view,name="signup"),
    path('',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('Settings/teacher',views.Settings,name="Settings"),
    path('Settings/student',views.Settings_student,name="Settings_student"),
    path('register/',views.register,name='register'),
    path('Profile/teacher/',views.profile_teacher,name='profile_teacher'),
    path('Profile/student/',views.profile_student,name='profile_student'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),

]