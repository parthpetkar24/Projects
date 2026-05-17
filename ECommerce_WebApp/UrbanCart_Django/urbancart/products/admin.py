from django.contrib import admin
from products.models import *
# Register your models here.
@admin.register(Product)
class ProductDisplay(admin.ModelAdmin):
    list_display=('product_id','product_name','seller','description','product_price','quantity','category')
