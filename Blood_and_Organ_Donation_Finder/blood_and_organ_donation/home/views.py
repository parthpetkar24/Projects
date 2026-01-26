from django.shortcuts import render,redirect
from .models import UserProfile,HospitalProfile,OrganDonation,BloodDonation,BloodRequest,OrganRequest,EmergencyBloodRequest,EmergencyOrganRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from geopy.geocoders import Nominatim
from random import choice
from string import ascii_letters,digits
import math

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url="login_user")
def donatepage(request):
    if request.method=="POST":
        donation_type = request.POST.get("donation_type")
        if donation_type not in ["blood", "organ"]:
            messages.error(request, "Invalid donation type")
            return redirect("donate")
        consent = request.POST.get("consent")
        if not consent:
            messages.error(request, "You must give consent to proceed")
            return redirect("donate")
        full_name=request.POST.get("full_name")
        aadhar_id=request.POST.get("aadhar_id")
        dob = request.POST.get("dob")
        if not dob:
            messages.error(request, "Date of birth is required")
            return redirect("donate")
        gender=request.POST.get("gender")
        city=request.POST.get("city")
        latitude, longitude=get_location(city)
        phone=request.POST.get("phone")
        weight_raw = request.POST.get("weight")
        try:
            weight = float(weight_raw)
        except (TypeError, ValueError):
            messages.error(request, "Please enter a valid weight.")
            return redirect("donate")
        medical_condition=request.POST.get("medical_condition")
        doc_report=request.FILES.get("doc_report")
        if donation_type=="blood":
            blood_group=request.POST.get("blood_group")
            BloodDonation.objects.create(
                full_name=full_name,
                aadhar_id=aadhar_id,
                dob=dob,
                gender=gender,
                city=city,
                latitude=latitude,
                longitude=longitude,
                phone=phone,
                blood_group=blood_group,
                weight=weight,
                medical_condition=medical_condition,
                doc_report=doc_report,
                form_id=create_form_id(BloodDonation)
            )
        elif donation_type=="organ":
            aliveordec=request.POST.get('aliveordec')
            organ=request.POST.get("organ")
            OrganDonation.objects.create(
                full_name=full_name,
                aadhar_id=aadhar_id,
                dob=dob,
                gender=gender,
                city=city,
                latitude=latitude,
                longitude=longitude,
                phone=phone,
                aliveordec=aliveordec,
                organ=organ,
                weight=weight,
                medical_condition=medical_condition,
                doc_report=doc_report,
                form_id=create_form_id(OrganDonation)
            )


        messages.success(request, "Donation registration submitted successfully")
        return redirect("user_dashboard")
    return render(request,"donate.html")

@login_required(login_url="login_user")
def requestpage(request):
    if request.method=="POST":
        request_type = request.POST.get("request_type")
        if request_type not in ["blood", "organ"]:
            messages.error(request, "Invalid donation type")
            return redirect("request")
        consent = request.POST.get("consent")
        if not consent:
            messages.error(request, "You must give consent")
            return redirect("request")
        full_name=request.POST.get("full_name")
        aadhar_id=request.POST.get("aadhar_id")
        dob = request.POST.get("dob")
        if not dob:
            messages.error(request, "Date of birth is required")
            return redirect("request")
        gender=request.POST.get("gender")
        city=request.POST.get("city")
        latitude, longitude=get_location(city)
        if latitude is None or longitude is None:
            messages.error(
                request,
                "Unable to detect location from the city name. Please enter a valid city."
                )
            return redirect("donate")
        phone=request.POST.get("phone")
        weight_raw = request.POST.get("weight")
        try:
            weight = float(weight_raw)
        except (TypeError, ValueError):
            messages.error(request, "Please enter a valid weight.")
            return redirect("donate")
        medical_condition=request.POST.get("medical_condition")
        doc_report=request.FILES.get("doc_report")
        if request_type=="blood":
            blood_group=request.POST.get("blood_group")
            BloodRequest.objects.create(
                full_name=full_name,
                aadhar_id=aadhar_id,
                dob=dob,
                gender=gender,
                city=city,
                latitude=latitude,
                longitude=longitude,
                phone=phone,
                blood_group=blood_group,
                weight=weight,
                medical_condition=medical_condition,
                doc_report=doc_report,
                form_id=create_form_id(BloodRequest)
            )
        elif request_type=="organ":
            organ=request.POST.get("organ")
            OrganRequest.objects.create(
                full_name=full_name,
                aadhar_id=aadhar_id,
                dob=dob,
                gender=gender,
                city=city,
                latitude=latitude,
                longitude=longitude,
                phone=phone,
                organ=organ,
                weight=weight,
                medical_condition=medical_condition,
                doc_report=doc_report,
                form_id=create_form_id(OrganRequest)
            )


        messages.success(request, "Request Made Successfully! ")
        return redirect("user_dashboard")
    return render(request,"request.html")

def emergency_request(request):
    if request.method=="POST":
        request_type = request.POST.get("request_type")
        if request_type not in ["blood", "organ"]:
            messages.error(request, "Invalid donation type")
            return redirect("emergency_request")
        full_name=request.POST.get("full_name")
        aadhar_id=request.POST.get("aadhar_id")
        dob = request.POST.get("dob")
        if not dob:
            messages.error(request, "Date of birth is required")
            return redirect("request")
        gender=request.POST.get("gender")
        city=request.POST.get("city")
        latitude, longitude=get_location(city)
        latitude, longitude = get_location(city)

        if latitude is None or longitude is None:
            messages.error(
                request,
                "Unable to detect location from the city name. Please enter a valid city."
                )
            return redirect("donate")

        phone=request.POST.get("phone")
        weight_raw = request.POST.get("weight")
        try:
            weight = float(weight_raw)
        except (TypeError, ValueError):
            messages.error(request, "Please enter a valid weight.")
            return redirect("donate")
        medical_condition=request.POST.get("medical_condition")
        doc_report=request.FILES.get("doc_report")
        if request_type=="blood":
            blood_group=request.POST.get("blood_group")
            EmergencyBloodRequest.objects.create(
                full_name=full_name,
                aadhar_id=aadhar_id,
                dob=dob,
                gender=gender,
                city=city,
                latitude=latitude,
                longitude=longitude,
                phone=phone,
                blood_group=blood_group,
                weight=weight,
                medical_condition=medical_condition,
                doc_report=doc_report,
                form_id=create_form_id(EmergencyBloodRequest)
            )
        elif request_type=="organ":
            organ=request.POST.get("organ")
            EmergencyOrganRequest.objects.create(
                full_name=full_name,
                aadhar_id=aadhar_id,
                dob=dob,
                gender=gender,
                city=city,
                latitude=latitude,
                longitude=longitude,
                phone=phone,
                organ=organ,
                weight=weight,
                medical_condition=medical_condition,
                doc_report=doc_report,
                form_id=create_form_id(EmergencyOrganRequest)
            )
        messages.success(request, "Request Made Successfully! ")
        return redirect("homepage")
    return render(request,"emergency_request.html")

def create_form_id(model, length=5):
    characters = ascii_letters + digits

    while True:
        form_id = "".join(choice(characters) for _ in range(length))
        if not model.objects.filter(form_id=form_id).exists():
            return form_id

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

def get_location(city):
    latitude = None
    longitude = None

    if not city:
        return None, None
    try:
        geolocator = Nominatim(
            user_agent="blood_and_organ_finder_app",
            timeout=10
        )
        location = geolocator.geocode(city)

        if location:
            latitude = location.latitude
            longitude = location.longitude

    except Exception as e:
        print("Geocoding error:", e)

    return latitude, longitude
    
def haversine_distance(lat1,lon1,lat2,lon2):
    if None in[lat1,lon1,lat2,lon2]:
        return None
    
    # Radius of Earth in km
    R=6371
    lat1,lon1,lat2,lon2=map(math.radians,[lat1,lon1,lat2,lon2])
    dlat=lat2-lat1
    dlon=lon2-lon1
    a=math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def get_nearby_applications(hospital,radius_km=10):
    lat=hospital.latitude
    lon=hospital.longitude
    results={
        "blood_donations":[],
        "blood_requests":[],
        "organ_donations":[],
        "organ_requests":[],
        "emergency_blood_requests":[],
        "emergency_organ_requests":[],
    }
    def filter_queryset(queryset,label):
        for obj in queryset.exclude(latitude=None,longitude=None):
            distance=haversine_distance(lat,lon,obj.latitude,obj.longitude)
            if distance and distance<=radius_km:
                results[label].append({
                    "form_id":obj.form_id,
                    "name":obj.full_name,
                    "city": obj.city,
                    "phone": obj.phone,
                    "distance": round(distance, 2),
                    "data": obj
                })
    filter_queryset(BloodDonation.objects.all(), "blood_donations")
    filter_queryset(BloodRequest.objects.all(), "blood_requests")
    filter_queryset(OrganDonation.objects.all(), "organ_donations")
    filter_queryset(OrganRequest.objects.all(), "organ_requests")
    filter_queryset(EmergencyBloodRequest.objects.all(), "emergency_blood_requests")
    filter_queryset(EmergencyOrganRequest.objects.all(), "emergency_organ_requests")

    return results

@login_required(login_url="login_user")
def user_dashboard(request):
    return render(request,"user_dashboard.html")

@login_required(login_url="login_hospital")
def hospital_dashboard(request):
    profile=request.user.hospitalprofile
    if request.method=="POST":
        profile.aplusunit=int(request.POST.get('aplusunit',profile.aplusunit))
        profile.aminusunit=request.POST.get('aminusunit',profile.aminusunit)
        profile.bplusunit=request.POST.get('bplusunit',profile.bplusunit)
        profile.bminusunit=request.POST.get('bminusunit',profile.bminusunit)
        profile.abplusunit=request.POST.get('abplusunit',profile.abplusunit)
        profile.abminusunit=request.POST.get('abminusunit',profile.abminusunit)
        profile.oplusunit=request.POST.get('oplusunit',profile.oplusunit)
        profile.ominusunit=request.POST.get('ominusunit',profile.ominusunit)
        profile.save()

        nearby_data=get_nearby_applications(profile)
    return render(request,"hospital_dashboard.html",nearby_data)


