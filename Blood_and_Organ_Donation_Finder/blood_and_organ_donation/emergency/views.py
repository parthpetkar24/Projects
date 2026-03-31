from django.shortcuts import render,redirect
from home.models import EmergencyBloodRequest,EmergencyOrganRequest
from home.views import create_form_id,get_location,find_and_notify_nearby_donors
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
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
            emergency_obj=EmergencyBloodRequest.objects.create(
                user=request.user if request.user.is_authenticated else None,
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
            emergency_obj=EmergencyOrganRequest.objects.create(
                user=request.user if request.user.is_authenticated else None,
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
        # Notify nearby donors
        find_and_notify_nearby_donors(emergency_obj)

        # Persist request identity in session so the status page can poll without auth
        request.session["emergency_form_id"]   = emergency_obj.form_id
        request.session["emergency_req_type"]  = request_type   # "blood" or "organ"
        request.session["emergency_req_phone"] = phone          # requester's contact

        return redirect("emergency_status")
    return render(request,"emergency_request.html")