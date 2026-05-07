from django.db import models

class Electronics(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"
    
class Camera_Accessories(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"
      
class TV_Video(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"
  
class Computers_Laptop(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Cooling_Air_Treatment(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Home_Appliances(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Health_Beauty_Hair(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Books(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Music(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Home_Lifestyle(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Home_Improvement_Tools(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Women_Style(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Men_Style(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Watches_Glasses(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Sports_Outdoor(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"

class Entertainment(models.Model):
    product_id=models.ForeignKey('sell.Product',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('sell.Seller_Info',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product_id.product_name}"
