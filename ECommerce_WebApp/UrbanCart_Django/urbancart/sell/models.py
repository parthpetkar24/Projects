from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError("Only PDF files allowed")

upi_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}$',
    message="Enter a valid UPI ID (e.g., name@bank)"
)

class Seller_Info(models.Model):
    seller_user=models.OneToOneField(User,on_delete=models.CASCADE)
    seller_id=models.CharField(max_length=6,primary_key=True)
    seller_first_name=models.CharField(max_length=100,default="NA")
    seller_last_name=models.CharField(max_length=100)
    seller_contact=PhoneNumberField()
    seller_verification=models.FileField(upload_to='seller/seller_verify',validators=[validate_pdf])
    address=models.TextField()
    seller_qr=models.FileField(upload_to='seller/seller_qr')
    upi_id = models.CharField(max_length=50,validators=[upi_validator],unique=True)