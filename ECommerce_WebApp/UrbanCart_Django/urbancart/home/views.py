from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import transaction
from buy.models import Buyer_Info
from sell.models import Seller_Info
import string
import random

# Functions

# Buyer Email Verification
buyer_email_validator=EmailValidator(
    message="Enter Valid Email Id"
)

# Seller Email Verification
seller_email_validator=EmailValidator(
    message="Enter Valid Email Id"
)

# Generate Buyer ID
def generatebuyerid():
    char_choices=string.ascii_uppercase+string.ascii_lowercase+string.digits
    charid=""
    for i in range(4):
        charid+=random.choice(char_choices)
    buyer_id="BUY"+charid
    exists=Buyer_Info.objects.filter(buyer_id=buyer_id).exists()
    if not exists:
        return buyer_id
    else:
        return generatebuyerid()

# Generate Seller ID
def generatesellerid():
    char_choices=string.ascii_uppercase+string.ascii_lowercase+string.digits
    charid=""
    for i in range(4):
        charid+=random.choice(char_choices)
    seller_id="SELL"+charid
    exists=Seller_Info.objects.filter(seller_id=seller_id).exists()
    if not exists:
        return seller_id
    else:
        return generatesellerid()


# Create your views here.
# Homepage
def homepage(request):
    return render(request,"home/homepage.html")

# User Account Creation & Authentication
def authenticateuser(request):
    if request.method=="POST":
        user_type=request.POST.get('user_type')
        auth_mode=request.POST.get('auth_mode')
        if user_type=="buyer":
            if auth_mode=="login":
                buyer_username=request.POST.get('buyer_username')
                buyer_password=request.POST.get('buyer_password')
                user=authenticate(username=buyer_username,password=buyer_password)
                if user:
                    login(request,user)
                    messages.success(request,"User Login Successful")
                    return redirect("home:homepage")
                else:
                    messages.error(request, "Invalid credentials")
                    return redirect("home:authenticate")
            elif auth_mode=="signup":
                buyer_id=generatebuyerid()
                buyer_first_name=request.POST.get('buyer_first_name')
                buyer_last_name=request.POST.get('buyer_last_name')
                buyer_username=request.POST.get('buyer_username')
                buyer_email_id=request.POST.get('buyer_email_id')
                buyer_password=request.POST.get('buyer_password')
                try:
                    buyer_email_validator(buyer_email_id)
                except ValidationError as e:
                    messages.error(request,"Invalid Credentials")
                    return redirect("home:authenticate")
                buyer_info=Buyer_Info.objects.filter(buyer_email_id=buyer_email_id).exists()
                if not buyer_info:
                    with transaction.atomic():
                        buyer_user=User.objects.create_user(username=buyer_username,email=buyer_email_id,password=buyer_password)
                        Buyer_Info.objects.create(
                            buyer_user=buyer_user,
                            buyer_id=buyer_id,
                            buyer_first_name=buyer_first_name,
                            buyer_last_name=buyer_last_name,
                            buyer_username=buyer_username,
                            buyer_email_id=buyer_email_id,
                        )
                        messages.success(request,"Account Created Successfully")
                        return redirect("home:authenticate")
                else:
                    messages.error(request,"User Already Exists")
        elif user_type=="seller":
            if auth_mode=="login":
                seller_username=request.POST.get('seller_username')
                seller_password=request.POST.get('seller_password')
                user=authenticate(username=seller_username,password=seller_password)
                if user:
                    login(request,user)
                    messages.success(request,"User Login Successful")
                    return redirect("home:homepage")
                else:
                    messages.error(request, "Invalid credentials")
                    return redirect("home:authenticate")
            elif auth_mode=="signup":
                seller_id=generatesellerid()
                seller_first_name=request.POST.get('seller_first_name')
                seller_last_name=request.POST.get('seller_last_name')
                seller_username=request.POST.get('seller_username')
                seller_email_id=request.POST.get('seller_email_id')
                seller_password=request.POST.get('seller_password')
                seller_verify=request.FILES.get('seller_verify')
                try:
                    seller_email_validator(seller_email_id)
                except ValidationError as e:
                    messages.error(request,"Invalid Credentials")
                    return redirect("home:authenticate")
                seller_info=Seller_Info.objects.filter(seller_email_id=seller_email_id).exists()
                if not seller_info:
                    with transaction.atomic():
                        seller_user=User.objects.create_user(username=seller_username,email=seller_email_id,password=seller_password)
                        Seller_Info.objects.create(
                            seller_user=seller_user,
                            seller_id=seller_id,
                            seller_first_name=seller_first_name,
                            seller_last_name=seller_last_name,
                            seller_username=seller_username,
                            seller_email_id=seller_email_id,
                            seller_verification=seller_verify,
                        )
                        messages.success(request,"Account Created Successfully")
                        return redirect("home:authenticate")
                else:
                    messages.error(request,"User Already Exists")
                    return redirect("home:authenticate")
    return render(request,"home/login_signup.html")

def logoutuser(request):
    logout(request) 
    messages.success(request, "You have been logged out successfully")
    return redirect("home:homepage")