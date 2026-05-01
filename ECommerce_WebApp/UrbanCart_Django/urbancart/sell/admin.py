from django.contrib import admin
from sell.models import *
# Register your models here.
@admin.register(Seller_Info)
class SellerDisplay(admin.ModelAdmin):
    list_display=('seller_id','seller_user','seller_first_name','seller_last_name','seller_contact','seller_verification','address','seller_qr','upi_id')