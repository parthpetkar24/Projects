from django.shortcuts import render

# Create your views here.
def cart_display(request):
    return render(request,'buy/cart.html')