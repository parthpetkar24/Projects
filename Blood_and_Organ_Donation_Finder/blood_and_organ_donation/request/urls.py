from django.urls import path
from . import views
app_name="request"

urlpatterns = [
    path('request/',views.requestpage,name='request'),
]