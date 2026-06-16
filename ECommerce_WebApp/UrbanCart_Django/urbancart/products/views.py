from django.shortcuts import render, get_object_or_404
from products.models import Product

category_map={"electronics":"Electronics","camera_accessories":"Camera & Accessories",
            "tv_video":"TV & Video","computers_laptops":"Computers & Laptops",
            "cooling_air_treatment":"Cooling & Air Treatment","home_appliances":"Home Appliances",
            "health_beauty_hair":"Health, Beauty & Hair","books":"Books","music":"Music",
            "home_lifestyle":"Home & Lifestyle","home_improvements_tools":"Home Improvements Tools",
            "women_style":"Women's Style","mens_style":"Men's Style","watches_glasses":"Watches & Glasses",
            "sports_outdoors":"Sports & Outdoors","entertainment":"Entertainment"}


# Create your views here.
def browse_products(request):
    products=Product.objects.prefetch_related("images")
    context={"products":products}
    return render(request,"products/product_browse.html",context)

def product_detail(request,product_id):
    product = get_object_or_404(
        Product,
        product_id=product_id
    )
    category=product.category
    if category in category_map:
        product_category=category_map[category]
    colors=product.color.split(",") if product.color else []
    sizes=product.size.split(",") if product.size else []
    context={"product":product,"product_category":product_category,"colors":colors,"sizes":sizes}
    return render(request,"products/product_detail.html",context)