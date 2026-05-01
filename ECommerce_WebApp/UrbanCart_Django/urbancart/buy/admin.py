from django.contrib import admin
from buy.models import *

# Register your models here.
@admin.register(Buyer_Info)
class BuyerDisplay(admin.ModelAdmin):
    list_display=('buyer_id','buyer_user','buyer_first_name','buyer_last_name','buyer_contact','address',)

