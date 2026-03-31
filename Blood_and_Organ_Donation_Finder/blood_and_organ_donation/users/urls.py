from django.urls import path
from . import views
app_name="users"

urlpatterns = [
    path('login_user/',views.login_user,name='login_user'),
    path('login_hospital/',views.login_hospital,name='login_hospital'),
    path('signup_user/',views.signup_user,name='signup_user'),
    path('signup_hospital/',views.signup_hospital,name='signup_hospital'),
    path('logout/', views.logout_user, name="logout"),
]