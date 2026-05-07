from django.contrib import admin
from buy.models import *

# Register your models here.
@admin.register(Buyer_Info)
class BuyerDisplay(admin.ModelAdmin):
    list_display=('buyer_id','buyer_user','buyer_first_name','buyer_last_name','buyer_contact','address_line1','address_line2','city','state','country','postal_code')

@admin.register(OrderProduct)
class OrderDisplay(admin.ModelAdmin):
    list_display=('order_id','buyer_id','seller_id','amount','quantity','payment_mode','payment_reference_id')

@admin.register(OrderLog)
class OrderLogDisplay(admin.ModelAdmin):
    list_display=('order_id','product_id','seller_id','buyer_id','quantity','amount','date','time')