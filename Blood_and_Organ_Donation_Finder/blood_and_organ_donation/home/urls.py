from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('homepage/',views.home, name='homepage'),
    path('donate/',views.donatepage,name='donate'),
    path('request/',views.requestpage,name='request'),
    path('emergency_request/',views.emergency_request,name='emergency_request'),
    path('login_user/',views.login_user,name='login_user'),
    path('login_hospital/',views.login_hospital,name='login_hospital'),
    path('signup_user/',views.signup_user,name='signup_user'),
    path('signup_hospital/',views.signup_hospital,name='signup_hospital'),
    path('logout/', views.logout_user, name="logout_user"),
    path('user_dashboard/',views.user_dashboard,name="user_dashboard"),
    path('hospital_dashboard/',views.hospital_dashboard,name="hospital_dashboard"),
    path('approve_application/', views.approve_application, name='approve_application'),
    path('reject_application/', views.reject_application, name='reject_application'),
]