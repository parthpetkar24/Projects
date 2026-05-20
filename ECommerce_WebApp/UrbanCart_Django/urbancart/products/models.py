from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_img(file):
    if not file.name.lower().endswith(('.png','.jpg','.jpeg','.svg','.gif')):
        raise ValidationError("Only Image File Format (png/jpg/jpeg/svg/gif) Allowed")
    
def product_image_path(instance, filename):
    return f'product/{instance.seller_id.seller_id}/{instance.product_id}/{filename}'


class Product(models.Model):
    product_id=models.CharField(max_length=8,primary_key=True)
    product_name=models.CharField(max_length=200)
    seller=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=15,decimal_places=3)
    quantity=models.IntegerField()
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
    color=models.CharField(max_length=100,blank=True,null=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    requirements=models.TextField(null=True,blank=True)


    def __str__(self):
        return f"{self.product_id} : {self.product_name}"
    
class ProductImage(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField( upload_to=product_image_path,validators=[validate_img])