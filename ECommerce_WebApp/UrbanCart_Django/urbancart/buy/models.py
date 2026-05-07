from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
# Create your models here.

def validate_profile(file):
    if not file.name.lower().endswith(('.png','.jpg','.jpeg','.svg','.gif')):
        raise ValidationError("Upload Appropriate Image Format")

def profile_pic_path(instance,filename):
    return f'buyer/{instance.buyer_id.buyer_id}/profile_pic/{filename}'

class Buyer_Info(models.Model):
    buyer_user=models.OneToOneField(User,on_delete=models.CASCADE)
    buyer_id=models.CharField(max_length=7,primary_key=True)
    buyer_first_name=models.CharField(max_length=70)
    buyer_last_name=models.CharField(max_length=70)
    buyer_contact=PhoneNumberField()
    profile_picture = models.ImageField(upload_to=profile_pic_path,blank=True,null=True)
    dob=models.DateField(null=True,blank=True)
    address_line1=models.CharField(max_length=250,null=True,blank=True)
    address_line2=models.CharField(max_length=250,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    state=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=70,default=" ")
    postal_code=models.DecimalField(max_digits=20,decimal_places=0,null=True,blank=True)
    
    def __str__(self):
        return f"{self.buyer_first_name} : {self.buyer_last_name}"
    
class OrderProduct(models.Model):
    order_id=models.CharField(max_length=6,primary_key=True)
    buyer_id=models.ForeignKey(Buyer_Info,on_delete=models.CASCADE)
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    amount=models.DecimalField(max_digits=15,decimal_places=3)
    payment_mode=models.CharField(
        max_length=30,
        choices=[
            ("upi_id","upi_id"),
            ("credit/debit","credit/debit"),
            ("qr_code","qr_code"),
            ("cash_on_delivery","cash_on_delivery")
        ]
    )
    payment_reference_id=models.DecimalField(max_digits=10,decimal_places=0)

    def __str__(self):
        return f"{self.order_id}"
    
class OrderLog(models.Model):
    order_id=models.ForeignKey(OrderProduct,on_delete=models.CASCADE)
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    buyer_id=models.ForeignKey(Buyer_Info,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    amount=models.DecimalField(max_digits=15,decimal_places=3)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return f"{self.order_id}"