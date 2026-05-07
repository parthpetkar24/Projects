from django.contrib import admin
from home.models import *

# Register your models here.



@admin.register(Electronics)
class Electronics_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Camera_Accessories)
class Camera_Accessories_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(TV_Video)
class TV_Video_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Computers_Laptop)
class Computers_Laptop_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Cooling_Air_Treatment)
class Cooling_Air_Treatment_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Home_Appliances)
class Home_Appliances_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Health_Beauty_Hair)
class Health_Beauty_Hair_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Books)
class Books_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Music)
class Music_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Home_Lifestyle)
class Home_Lifestyle_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Home_Improvement_Tools)
class Home_Improvement_Tools_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Women_Style)
class Women_Style_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Men_Style)
class Men_Style_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Watches_Glasses)
class Watches_Glasses_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Sports_Outdoor)
class Sports_Outdoor_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

@admin.register(Entertainment)
class Entertainment_List(admin.ModelAdmin):
    list_display=['product_id','seller_id',]

