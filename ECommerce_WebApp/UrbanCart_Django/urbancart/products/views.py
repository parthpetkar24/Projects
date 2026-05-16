from django.shortcuts import render

# Create your views here.
def browse_products(request):
    return render(request,"products/product_browse.html")

def product_detail(request):
    return render(request,"products/product_detail.html")