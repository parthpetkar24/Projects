from django.shortcuts import render,redirect
from home.models import BloodRequest,OrganRequest
from home.views import create_form_id,get_location
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="users:login_user")
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
