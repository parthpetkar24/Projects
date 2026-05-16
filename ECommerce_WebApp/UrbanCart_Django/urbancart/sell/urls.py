from django.urls import path
from . import views;

app_name="sell"

urlpatterns=[
    path('',views.seller_dashboard,name='seller_dashboard'),
]