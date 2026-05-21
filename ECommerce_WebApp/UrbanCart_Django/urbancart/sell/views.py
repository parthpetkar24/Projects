from django.shortcuts import render,redirect
from sell.models import Seller_Info,Inventory,SellingLog
from products.models import Product,ProductImage
from home.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
import string
from random import choice

def productidgeneration():
    characters=string.ascii_uppercase+string.ascii_lowercase+string.digits
    char_id=''
    for i in range(4):
        char_id+=choice(characters)
    product_id="PROD"+char_id
    exists=Product.objects.filter(product_id=product_id).exists()
    if not exists:
        return product_id
    else:
        return productidgeneration()
    
CATEGORY_MAP={
    "electronics": Electronics,
    "camera_accessories":Camera_Accessories,
    "tv_video":TV_Video,
    "computers_laptops":Computers_Laptop,
    "cooling_air_treatment":Cooling_Air_Treatment,
    "home_appliances":Home_Appliances,
    "health_beauty_hair":Health_Beauty_Hair,
    "books":Books,
    "music":Music,
    "home_lifestyle":Home_Lifestyle,
    "home_improvements_tools":Home_Improvement_Tools,
    "women_style":Women_Style,
    "mens_style":Men_Style,
    "watches_glasses":Watches_Glasses,
    "sports_outdoors":Sports_Outdoor,
    "entertainment":Entertainment,
}
    
# Create your views here.
@login_required(login_url="home:authenticate")
def seller_dashboard(request):
    seller=Seller_Info.objects.get(seller_user=request.user)
    seller_revenue=seller.sells_amount
    inventory=Inventory.objects.all()
    context={"seller_revenue":seller_revenue,"inventory":inventory}
    return render(request,"sell/sell_dashboard.html",context)

@login_required(login_url="home:authenticate")
def add_product(request):
    if request.method=="POST":
        product_id=productidgeneration()
        product_name=request.POST.get('product_name')
        metadata=request.POST.get('metadata')
        description=request.POST.get('description')
        price=request.POST.get('price')
        category=request.POST.get('category')
        quantity=request.POST.get('quantity')
        images = request.FILES.getlist("product_images")
        # Maximum 4 validation
        if len(images) > 4:
            messages.error(request,"Maximum 4 images allowed")
            return redirect("sell:seller_dashboard")
        color=request.POST.get("color")
        size=request.POST.get("size")
        requirements=request.POST.get("requirements")
        model_class = CATEGORY_MAP.get(category)
        with transaction.atomic():
            product=Product.objects.create(
                product_id=product_id,
                product_name=product_name,
                seller=Seller_Info.objects.get(seller_user=request.user),
                product_price=price,
                quantity=quantity,
                meta_data=metadata,
                description=description,
                category=category,
                color=color,
                size=size,
                requirements=requirements,
            )
            for image in images:
                ProductImage.objects.create(
                product=product,
                image=image
            )
            if model_class:
                model_class.objects.create( seller=Seller_Info.objects.get(seller_user=request.user), product=product)
            else:
                messages.error(request, "Invalid category")
            Inventory.objects.create(product=product,quantity=quantity,amount=price)
        messages.success(request,"Product Added Successfully")
        
        return redirect("sell:seller_dashboard")
        
    return redirect("sell:seller_dashboard")
