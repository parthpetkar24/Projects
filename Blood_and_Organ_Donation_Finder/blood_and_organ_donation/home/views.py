from django.shortcuts import render
from .models import BloodDonation,OrganDonation,EmergencyNotification
from geopy.geocoders import Nominatim
from random import choice
from string import ascii_letters,digits
import math

# Create your views here.
def home(request):
    return render(request,'home.html')

def create_form_id(model, length=5):
    characters = ascii_letters + digits

    while True:
        form_id = "".join(choice(characters) for _ in range(length))
        if not model.objects.filter(form_id=form_id).exists():
            return form_id

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
        for obj in queryset.filter(status='pending', is_active=True).exclude(latitude=None, longitude=None):
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

def find_and_notify_nearby_donors(emergency_obj, radius_km=50):

    lat = emergency_obj.latitude
    lon = emergency_obj.longitude

    if hasattr(emergency_obj, "blood_group"):
        donors = BloodDonation.objects.filter(
            status='approved',
            blood_group=emergency_obj.blood_group
        ).exclude(latitude=None, longitude=None)

    else:
        donors = OrganDonation.objects.filter(
            status='approved',
            organ=emergency_obj.organ
        ).exclude(latitude=None, longitude=None)

    for donor in donors:
        distance = haversine_distance(lat, lon, donor.latitude, donor.longitude)

        if distance is not None and distance <= radius_km:
            EmergencyNotification.objects.create(
                donor=donor.user,
                blood_request=emergency_obj if hasattr(emergency_obj, "blood_group") else None,
                organ_request=emergency_obj if hasattr(emergency_obj, "organ") else None
            )