from django.shortcuts import render,redirect
from .models import UserProfile,HospitalProfile,OrganDonation,BloodDonation,BloodRequest,OrganRequest,EmergencyBloodRequest,EmergencyOrganRequest,HospitalNews
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from geopy.geocoders import Nominatim
from random import choice
from string import ascii_letters,digits
import math
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.conf import settings
import os

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
                user=request.user,
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
                user=request.user,
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
                user=request.user,
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
                user=request.user,
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
                user=request.user,
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
                user=request.user,
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

def get_nearby_applications(hospital, radius_km=50):
    lat = hospital.latitude
    lon = hospital.longitude
    
    results = {
        "blood_donations": [],
        "blood_requests": [],
        "organ_donations": [],
        "organ_requests": [],
        "emergency_blood_requests": [],
        "emergency_organ_requests": [],
    }
    
    def filter_queryset(queryset, label):
        # Only fetch pending applications
        for obj in queryset.filter(status='pending').exclude(latitude=None, longitude=None):
            distance = haversine_distance(lat, lon, obj.latitude, obj.longitude)
            if distance is not None and distance <= radius_km:
                results[label].append({
                    "form_id": obj.form_id,
                    "name": obj.full_name,
                    "city": obj.city,
                    "phone": obj.phone,
                    "distance": round(distance, 2),
                    "data": obj,
                    "status": obj.status,
                })
        # Sort by distance (nearest first)
        results[label].sort(key=lambda x: x['distance'])

    # Filter all types of applications
    filter_queryset(BloodDonation.objects.all(), "blood_donations")
    filter_queryset(BloodRequest.objects.all(), "blood_requests")
    filter_queryset(OrganDonation.objects.all(), "organ_donations")
    filter_queryset(OrganRequest.objects.all(), "organ_requests")
    filter_queryset(EmergencyBloodRequest.objects.all(), "emergency_blood_requests")
    filter_queryset(EmergencyOrganRequest.objects.all(), "emergency_organ_requests")

    return results

@login_required(login_url="login_user")
def user_dashboard(request):
    news_list = HospitalNews.objects.all().order_by("-created_at")
    user = request.user

    context = {
        "blood_donations": BloodDonation.objects.filter(user=user).order_by("-approved_at"),
        "organ_donations": OrganDonation.objects.filter(user=user).order_by("-approved_at"),
        "blood_requests": BloodRequest.objects.filter(user=user).order_by("-approved_at"),
        "organ_requests": OrganRequest.objects.filter(user=user).order_by("-approved_at"),
        "emergency_blood_requests": EmergencyBloodRequest.objects.filter(user=user).order_by("-approved_at"),
        "emergency_organ_requests": EmergencyOrganRequest.objects.filter(user=user).order_by("-approved_at"),
        "news_list": news_list,
    }
    return render(request, "user_dashboard.html", context)

@login_required(login_url="login_hospital")
def hospital_dashboard(request):
    profile=request.user.hospitalprofile
    if request.method=="POST":
        profile.aplusunit=int(request.POST.get('aplusunit',profile.aplusunit))
        profile.aminusunit=int(request.POST.get('aminusunit',profile.aminusunit))
        profile.bplusunit=int(request.POST.get('bplusunit',profile.bplusunit))
        profile.bminusunit=int(request.POST.get('bminusunit',profile.bminusunit))
        profile.abplusunit=int(request.POST.get('abplusunit',profile.abplusunit))
        profile.abminusunit=int(request.POST.get('abminusunit',profile.abminusunit))
        profile.oplusunit=int(request.POST.get('oplusunit',profile.oplusunit))
        profile.ominusunit=int(request.POST.get('ominusunit',profile.ominusunit))
        profile.save()
    if request.method == "POST" and "news_title" in request.POST:
        HospitalNews.objects.create(
            hospital=profile,
            title=request.POST.get("news_title"),
            content=request.POST.get("news_content")
        )
        messages.success(request,'News Published Successfully!')
        return redirect('hospital_dashboard')
    nearby_data = get_nearby_applications(profile)  
    news_list = HospitalNews.objects.filter(
        hospital=profile
    ).order_by("-created_at")

    context = {
        **nearby_data,
        "news_list": news_list
    }
    return render(request, "hospital_dashboard.html", context)  

@login_required(login_url="login_hospital")
@require_POST
def approve_application(request):
    app_type = request.POST.get('app_type')
    form_id = request.POST.get('form_id')
    date = request.POST.get("date")
    time = request.POST.get("time")

    if not date or not time:
        return JsonResponse({
            "success": False,
            "error": "Appointment date and time required"
        })
    
    try:
        hospital_profile = request.user.hospitalprofile
    except HospitalProfile.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Hospital profile not found'})
    
    # Map application types to models
    model_map = {
        'blood_donation': BloodDonation,
        'blood_request': BloodRequest,
        'organ_donation': OrganDonation,
        'organ_request': OrganRequest,
        'emergency_blood_request': EmergencyBloodRequest,
        'emergency_organ_request': EmergencyOrganRequest,
    }
    
    if app_type not in model_map:
        return JsonResponse({'success': False, 'error': 'Invalid application type'})
    
    try:
        application = model_map[app_type].objects.get(form_id=form_id)
        application.status = 'approved'
        application.approved_by = hospital_profile
        application.approved_at = timezone.now()
        application.appointment_date = date
        application.appointment_time = time
        filename = f"{form_id}_appointment.pdf"
        folder_path = os.path.join(settings.MEDIA_ROOT, "appointments")
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, filename)

        pdf = canvas.Canvas(file_path, pagesize=A4)
        pdf.setFont("Helvetica", 12)

        pdf.drawString(50, 800, "APPOINTMENT CONFIRMATION")
        pdf.drawString(50, 770, f"Hospital Name: {hospital_profile.hospital_name}")
        pdf.drawString(50, 750, f"Hospital City: {hospital_profile.city}")
        pdf.drawString(50, 720, f"Applicant Name: {application.full_name}")
        pdf.drawString(50, 700, f"Form ID: {application.form_id}")
        pdf.drawString(50, 680, f"Appointment Date: {application.appointment_date}")
        pdf.drawString(50, 660, f"Appointment Time: {application.appointment_time}")

        pdf.showPage()
        pdf.save()

        application.appointment_pdf = f"appointments/approved/{filename}"
        application.save()
        
        messages.success(request, f"Application {form_id} approved successfully")
        return JsonResponse({'success': True})
    except model_map[app_type].DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Application not found'})

@login_required(login_url="login_hospital")
@require_POST
def reject_application(request):

    app_type = request.POST.get('app_type')
    form_id = request.POST.get('form_id')
    
    try:
        hospital_profile = request.user.hospitalprofile
    except HospitalProfile.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Hospital profile not found'})
    
    model_map = {
        'blood_donation': BloodDonation,
        'blood_request': BloodRequest,
        'organ_donation': OrganDonation,
        'organ_request': OrganRequest,
        'emergency_blood_request': EmergencyBloodRequest,
        'emergency_organ_request': EmergencyOrganRequest,
    }
    
    if app_type not in model_map:
        return JsonResponse({'success': False, 'error': 'Invalid application type'})
    
    try:
        application = model_map[app_type].objects.get(form_id=form_id)
        application.status = 'rejected'
        application.approved_by = hospital_profile
        application.approved_at = timezone.now()
        application.save()
        
        messages.success(request, f"Application {form_id} rejected")
        return JsonResponse({'success': True})
    except model_map[app_type].DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Application not found'})
