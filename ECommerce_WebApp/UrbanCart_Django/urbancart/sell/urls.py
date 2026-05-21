from django.urls import path
from . import views;

app_name="sell"

urlpatterns=[
    path('',views.seller_dashboard,name='seller_dashboard'),
    path('product/add/',views.add_product,name="add_product"),

]