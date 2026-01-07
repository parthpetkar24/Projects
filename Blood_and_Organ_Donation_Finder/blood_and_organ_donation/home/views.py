from django.shortcuts import render,redirect
from .models import UserProfile,HospitalProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from geopy.geocoders import Nominatim
from string import ascii_letters,ascii_lowercase

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url="login_user")
def donatepage(request):
    if request.method=="POST":
        donation_type = request.POST.get("donation_type")
        dob = request.POST.get("dob")
        consent = request.POST.get("consent")

        if not consent:
            messages.error(request, "You must give consent to proceed")
            return redirect("donate")

        if not dob:
            messages.error(request, "Date of birth is required")
            return redirect("donate")

        dob = date.fromisoformat(dob)
        today = date.today()

        age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
        )

        if age < 18:
            messages.error(request, "Donor must be at least 18 years old")
            return redirect("donate")

        request.session["donation_type"] = donation_type

        messages.success(request, "Donation registration submitted successfully")
        return redirect("homepage")
    return render(request,"donate.html")

def requestpage(request):
    return render(request,"request.html")

def login_user(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user:
            login(request, user)
            messages.success(request,"Login Successfull!")
            return redirect("homepage")

        messages.error(request, "Invalid credentials")
        return redirect("login_user")
    return render(request, "login_user.html")

def login_hospital(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user:
            login(request, user)
            return redirect("homepage")

        messages.error(request, "Invalid credentials")
        return redirect("login_hospital")
    return render(request, "login_hospital.html")

def signup_user(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        city = request.POST.get("city")
        latitude = None
        longitude = None

        if city:
            geolocator = Nominatim(
                user_agent="blood_and_organ_finder_app",
                timeout=10
            )
            location = geolocator.geocode(city)
            if location:
                latitude = location.latitude
                longitude = location.longitude

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
        latitude = None
        longitude = None

        if city:
            geolocator = Nominatim(
                user_agent="blood_and_organ_finder_app",
                timeout=10
            )
            location = geolocator.geocode(city)
            if location:
                latitude = location.latitude
                longitude = location.longitude
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

@login_required(login_url="login_user")
def user_dashboard(request):
    return render(request,"user_dashboard.html")



