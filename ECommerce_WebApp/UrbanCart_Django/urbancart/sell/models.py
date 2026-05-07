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

def product_image_path(instance, filename):
    return f'product/{instance.seller_id.seller_id}/{instance.product_id}/{filename}'

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
    
    def __str__(self):
        return f"{self.seller_first_name} : {self.seller_last_name}"

class Product(models.Model):
    product_id=models.CharField(max_length=5,primary_key=True)
    product_name=models.CharField(max_length=200)
    seller_id=models.ForeignKey(Seller_Info,on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=15,decimal_places=3)
    quantity=models.IntegerField()
    images=models.ImageField(upload_to=product_image_path,validators=[validate_img])
    meta_data=models.CharField(max_length=300)
    description=models.TextField()
    category=models.CharField(
        max_length=50,
        choices=[
            ("electronics","electronics"),("camera_accessories","camera_accessories"),
            ("tv_video","tv_video"),("computers_laptops","computers_laptops"),
            ("cooling_air_treatment","cooling_air_treatment"),("home_appliances","home_appliances"),
            ("health_beauty_hair","health_beauty_hair"),("books","books"),("music","music"),
            ("home_lifestyle","home_lifestyle"),("home_improvements_tools","home_improvements_tools"),
            ("women_style","women_style"),("mens_style","mens_style"),("watches_glasses","watches_glasses"),
            ("sports_outdoors","sports_outdoors"),("entertainment","entertainment")
        ],
        null=True,
    )

    def __str__(self):
        return f"{self.product_id} : {self.product_name}"
    
class SellingLog(models.Model):
    order_id=models.ForeignKey('buy.OrderProduct',on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    seller_id=models.ForeignKey(Seller_Info,on_delete=models.CASCADE)
    buyer_id=models.ForeignKey('buy.Buyer_Info',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    amount=models.DecimalField(max_digits=15,decimal_places=3)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return f"{self.order_id}"