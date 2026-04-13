from django.shortcuts import render,redirect
from home.models import HospitalProfile,OrganDonation,BloodDonation,BloodRequest,OrganRequest,EmergencyBloodRequest,EmergencyOrganRequest,HospitalNews
from home.views import get_nearby_applications
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.conf import settings
import os

# Create your views here.
@login_required(login_url="users:login_hospital")
def hospital_dashboard(request):
    profile=request.user.hospitalprofile
    
    if request.method == "POST" and "news_title" in request.POST:
        HospitalNews.objects.create(
            hospital=profile,
            title=request.POST.get("news_title"),
            content=request.POST.get("news_content")
        )
        messages.success(request,'News Published Successfully!')
        return redirect('hospital_dashboard')
    elif request.method=="POST":
        profile.aplusunit=int(request.POST.get('aplusunit',profile.aplusunit))
        profile.aminusunit=int(request.POST.get('aminusunit',profile.aminusunit))
        profile.bplusunit=int(request.POST.get('bplusunit',profile.bplusunit))
        profile.bminusunit=int(request.POST.get('bminusunit',profile.bminusunit))
        profile.abplusunit=int(request.POST.get('abplusunit',profile.abplusunit))
        profile.abminusunit=int(request.POST.get('abminusunit',profile.abminusunit))
        profile.oplusunit=int(request.POST.get('oplusunit',profile.oplusunit))
        profile.ominusunit=int(request.POST.get('ominusunit',profile.ominusunit))
        profile.save()
    nearby_data = get_nearby_applications(profile)  
    news_list = HospitalNews.objects.filter(
        hospital=profile
    ).order_by("-created_at")

    context={ **nearby_data,"news_list": news_list}
    return render(request, "hospital_dashboard.html", context)  

@login_required(login_url="users:login_hospital")
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

        application.appointment_pdf = f"appointments/{filename}"
        application.save()
        pdf_url = f"{settings.MEDIA_URL}appointments/{filename}"  # ✅ Build the URL

        return JsonResponse({'success': True, 'pdf_url': pdf_url})
    except model_map[app_type].DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Application not found'})

@login_required(login_url="users:login_hospital")
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