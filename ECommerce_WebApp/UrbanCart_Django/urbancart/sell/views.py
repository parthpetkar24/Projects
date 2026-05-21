from django.shortcuts import render,redirect
from sell.models import Seller_Info
from products.models import Product,ProductImage
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
    
# Create your views here.
@login_required(login_url="home:authenticate")
def seller_dashboard(request):
    seller=Seller_Info.objects.get(seller_user=request.user)
    seller_revenue=seller.sells_amount
    return render(request,"sell/sell_dashboard.html",{"seller_revenue":seller_revenue})

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
        messages.success(request,"Product Added Successfully")
        return redirect("sell:seller_dashboard")
    return redirect("sell:seller_dashboard")
