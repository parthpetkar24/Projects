from django.urls import path
from . import views

app_name="products"

urlpatterns=[
    path('',views.browse_products,name="browse_products"),
    path('detail/<str:product_id>/',views.product_detail,name="detail")
]