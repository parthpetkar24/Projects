from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='home:authenticate')
def cart_display(request):
    return render(request,'buy/cart.html')