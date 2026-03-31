from django.urls import path
from . import views
app_name="emergency"

urlpatterns = [
    path('emergency_request/',views.emergency_request,name='emergency_request'),
]