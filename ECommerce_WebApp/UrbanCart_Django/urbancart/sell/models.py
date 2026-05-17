from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_pdf(file):
    if not file.name.lower().endswith('.pdf'):
        raise ValidationError("Only PDF files allowed")

def validate_img(file):
    if not file.name.lower().endswith(('.png','.jpg','.jpeg','.svg','.gif')):
        raise ValidationError("Only Image File Format (png/jpg/jpeg/svg/gif) Allowed")

upi_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}$',
    message="Enter a valid UPI ID (e.g., name@bank)"
)

def seller_verification_path(instance,filename):
    return f'seller/{instance.seller_id.seller_id}/seller_verify/{filename}'

def seller_qr_path(instance,filename):
    return f'seller/{instance.seller_id.seller_id}/seller_qr/{filename}'

class Seller_Info(models.Model):
    seller_user=models.OneToOneField(User,on_delete=models.CASCADE)
    seller_id=models.CharField(max_length=6,primary_key=True)
    seller_first_name=models.CharField(max_length=100,default="NA")
    seller_last_name=models.CharField(max_length=100)
    seller_contact=PhoneNumberField()
    seller_verification=models.FileField(upload_to=seller_verification_path,validators=[validate_pdf])
    address=models.TextField()
    seller_qr=models.FileField(upload_to=seller_qr_path,validators=[validate_img])
    upi_id = models.CharField(max_length=50,validators=[upi_validator],unique=True)
    sells_amount=models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    
    def __str__(self):
        return f"{self.seller_first_name} : {self.seller_last_name}"

    
class SellingLog(models.Model):
    order=models.ForeignKey('buy.OrderProduct',on_delete=models.CASCADE)
    product=models.ForeignKey('products.Product',on_delete=models.CASCADE)
    seller=models.ForeignKey(Seller_Info,on_delete=models.CASCADE)
    buyer=models.ForeignKey('buy.Buyer_Info',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    amount=models.DecimalField(max_digits=15,decimal_places=3)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return f"{self.order_id}"