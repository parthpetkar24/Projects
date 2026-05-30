from django.shortcuts import render, get_object_or_404
from products.models import Product


# Create your views here.
def browse_products(request):
    products=Product.objects.prefetch_related("images")
    return render(request,"products/product_browse.html",{"products":products})

def product_detail(request,product_id):
    product = get_object_or_404(
        Product,
        product_id=product_id
    )
    return render(request,"products/product_detail.html",{"product":product})