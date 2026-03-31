from django.shortcuts import render,redirect
from home.models import UserProfile,HospitalProfile
from home.views import create_form_id,get_location
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user:
            login(request, user)
            messages.success(request,"Login Successfull!")
            return redirect("user_dashboard")

        messages.error(request, "Invalid credentials")
        return redirect("login_user")
    return render(request, "login_user.html")

def login_hospital(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user=authenticate(username=email,password=password)
        if user:
            login(request,user)
            messages.success(request,"Login Successfull!")
            return redirect("hospital_dashboard")
        
        messages.error(request,"Invalid credentials")
        return redirect("login_hospital")
    return render(request,"login_hospital.html")

def signup_user(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        city = request.POST.get("city")
        latitude, longitude=get_location(city)
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup_user")
        
        user=User.objects.create_user(
            username=email,
            email=email,
            password=password,
        )
        UserProfile.objects.create(
            user=user,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            blood_group = request.POST.get("blood_group"),
            city=city,
            longitude=longitude,
            latitude=latitude,
        )
        messages.success(request,'Account Created Successfully!')
        return redirect('login_user')
    return render(request, "signup_user.html")

def signup_hospital(request):
    if request.method=="POST":
        hospital_email=request.POST.get('hospital_email')
        hospital_password=request.POST.get('hospital_password')
        city=request.POST.get('city')
        latitude, longitude=get_location(city)
        if User.objects.filter(username=hospital_email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup_hospital")
        
        user=User.objects.create_user(
            username=hospital_email,
            email=hospital_email,
            password=hospital_password,
        )
        HospitalProfile.objects.create(
            user=user,
            hospital_name=request.POST.get('hospital_name'),
            registration_id=request.POST.get('registration_id'),
            contact_number=request.POST.get('contact_number'),
            license=request.FILES.get('license'),
            city=city,
            longitude=longitude,
            latitude=latitude,
        )
        messages.success(request,'Account Created Successfully!')
        return redirect('login_hospital')
    return render(request, "signup_hospital.html")

def logout_user(request):
    logout(request) 
    messages.success(request, "You have been logged out successfully")
    return redirect("homepage")
