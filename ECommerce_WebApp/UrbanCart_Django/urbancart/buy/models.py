from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Buyer_Info(models.Model):
    buyer_user=models.OneToOneField(User,on_delete=models.CASCADE)
    buyer_id=models.CharField(max_length=7,primary_key=True)
    buyer_first_name=models.CharField(max_length=70)
    buyer_last_name=models.CharField(max_length=70)
    buyer_contact=PhoneNumberField()
    address=models.TextField()