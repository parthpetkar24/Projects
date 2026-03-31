from django.shortcuts import render,redirect
from home.models import OrganDonation,BloodDonation
from home.views import create_form_id,get_location
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="users:login_user")
def donatepage(request):
    if request.method=="POST":
        donation_type = request.POST.get("donation_type")
        if donation_type not in ["blood", "organ"]:
            messages.error(request, "Invalid donation type")
            return redirect("donate:donate")
        consent = request.POST.get("consent")
        if not consent:
            messages.error(request, "You must give consent to proceed")
            return redirect("donate:donate")
        full_name=request.POST.get("full_name")
        aadhar_id=request.POST.get("aadhar_id")
        dob = request.POST.get("dob")
        if not dob:
            messages.error(request, "Date of birth is required")
            return redirect("donate:donate")
        gender=request.POST.get("gender")
        city=request.POST.get("city")
        latitude, longitude=get_location(city)
        phone=request.POST.get("phone")
        weight_raw = request.POST.get("weight")
        try:
            weight = float(weight_raw)
        except (TypeError, ValueError):
            messages.error(request, "Please enter a valid weight.")
            return redirect("donate:donate")
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
        return redirect("user_dashboard:user_dashboard")
    return render(request,"donate.html")