from django.urls import path
from . import views;

app_name="home"

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('authenticate/',views.authenticateuser,name="authenticate"),
    path('logout/',views.logoutuser,name="logout")
]