from django.urls import path
from . import views
app_name="hospital_dashboard"

urlpatterns = [
    path('',views.hospital_dashboard,name="hospital_dashboard"),
    path('approve_application/', views.approve_application, name='approve_application'),
    path('reject_application/', views.reject_application, name='reject_application'),
]