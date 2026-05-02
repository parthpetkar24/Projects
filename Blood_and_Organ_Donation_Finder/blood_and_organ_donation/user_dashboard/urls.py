from django.urls import path
from . import views
app_name="user_dashboard"

urlpatterns = [
    path('user_dashboard/',views.user_dashboard,name="user_dashboard"),
    path("accept-emergency/", views.accept_emergency, name="accept_emergency"),
    path('emergency_status/', views.emergency_status, name='emergency_status'),
    path('check_emergency_status/', views.check_emergency_status, name='check_emergency_status'),
    path('clear-application/', views.clear_application, name='clear_application'),
]