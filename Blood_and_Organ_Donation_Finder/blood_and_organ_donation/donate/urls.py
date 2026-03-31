from django.urls import path
from . import views
app_name="donate"

urlpatterns = [
    path('donate/',views.donatepage,name='donate')
]