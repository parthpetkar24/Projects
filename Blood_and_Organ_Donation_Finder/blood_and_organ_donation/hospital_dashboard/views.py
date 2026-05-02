from django.shortcuts import render,redirect
from home.models import HospitalProfile,OrganDonation,BloodDonation,BloodRequest,OrganRequest,EmergencyBloodRequest,EmergencyOrganRequest,HospitalNews
from home.views import get_nearby_applications
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings
import os
from datetime import datetime

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

        # ── Professional PDF Generation ──────────────────────────────
        width, height = A4
        pdf = canvas.Canvas(file_path, pagesize=A4)
        pdf.setTitle(f"Appointment Confirmation - {form_id}")

        # ── Color palette ──
        PRIMARY    = HexColor("#B71C1C")   # deep medical red
        SECONDARY  = HexColor("#D32F2F")
        DARK       = HexColor("#212121")
        GREY       = HexColor("#757575")
        LIGHT_GREY = HexColor("#F5F5F5")
        WHITE      = HexColor("#FFFFFF")

        # ── Top accent bar ──
        pdf.setFillColor(PRIMARY)
        pdf.rect(0, height - 18*mm, width, 18*mm, fill=1, stroke=0)

        # ── Header text on bar ──
        pdf.setFillColor(WHITE)
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(25*mm, height - 13*mm, "MediFlow")
        pdf.setFont("Helvetica", 9)
        pdf.drawRightString(width - 25*mm, height - 10*mm, "Appointment Confirmation")
        pdf.drawRightString(width - 25*mm, height - 14*mm, f"Document ID: {form_id}")

        # ── Thin accent line under bar ──
        pdf.setStrokeColor(SECONDARY)
        pdf.setLineWidth(2)
        pdf.line(25*mm, height - 20*mm, width - 25*mm, height - 20*mm)

        # ── Hospital Information ──
        y = height - 32*mm
        pdf.setFillColor(DARK)
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(25*mm, y, hospital_profile.hospital_name.upper())
        y -= 6*mm
        pdf.setFont("Helvetica", 9)
        pdf.setFillColor(GREY)
        pdf.drawString(25*mm, y, f"City: {hospital_profile.city}    |    Contact: {hospital_profile.contact_number}")
        y -= 4*mm
        pdf.drawString(25*mm, y, f"Registration ID: {hospital_profile.registration_id}")

        # ── Section: Patient Details ──
        y -= 14*mm
        pdf.setFillColor(PRIMARY)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(25*mm, y, "PATIENT DETAILS")
        y -= 2*mm
        pdf.setStrokeColor(PRIMARY)
        pdf.setLineWidth(0.8)
        pdf.line(25*mm, y, width - 25*mm, y)

        # ── Details table ──
        app_type_display = app_type.replace('_', ' ').title()
        details = [
            ("Full Name",        application.full_name),
            ("Form ID",          application.form_id),
            ("Application Type", app_type_display),
            ("City",             getattr(application, 'city', '—')),
            ("Phone",            getattr(application, 'phone', '—')),
        ]

        # Add type-specific field
        if hasattr(application, 'blood_group') and application.blood_group:
            details.append(("Blood Group", application.blood_group))
        if hasattr(application, 'organ') and application.organ:
            details.append(("Organ", application.organ))

        y -= 6*mm
        row_h = 8*mm
        col1_x = 25*mm
        col2_x = 80*mm
        table_w = width - 50*mm

        for i, (label, value) in enumerate(details):
            # Alternating row background
            if i % 2 == 0:
                pdf.setFillColor(LIGHT_GREY)
                pdf.rect(col1_x, y - 2*mm, table_w, row_h, fill=1, stroke=0)

            pdf.setFillColor(DARK)
            pdf.setFont("Helvetica-Bold", 9)
            pdf.drawString(col1_x + 3*mm, y + 1*mm, label)
            pdf.setFont("Helvetica", 9)
            pdf.drawString(col2_x, y + 1*mm, str(value or '—'))
            y -= row_h

        # ── Section: Appointment Details ──
        y -= 10*mm
        pdf.setFillColor(PRIMARY)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(25*mm, y, "APPOINTMENT SCHEDULE")
        y -= 2*mm
        pdf.setStrokeColor(PRIMARY)
        pdf.setLineWidth(0.8)
        pdf.line(25*mm, y, width - 25*mm, y)

        # Appointment box
        y -= 4*mm
        box_h = 22*mm
        pdf.setStrokeColor(SECONDARY)
        pdf.setLineWidth(1)
        pdf.setFillColor(HexColor("#FFF5F5"))
        pdf.roundRect(25*mm, y - box_h, table_w, box_h, 3*mm, fill=1, stroke=1)

        # Date & Time inside box
        pdf.setFillColor(DARK)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(30*mm, y - 8*mm, f"Date:  {application.appointment_date}")
        pdf.drawString(30*mm, y - 16*mm, f"Time:  {application.appointment_time}")

        # Status badge
        pdf.setFillColor(HexColor("#2E7D32"))
        pdf.roundRect(width - 70*mm, y - 16*mm, 30*mm, 10*mm, 2*mm, fill=1, stroke=0)
        pdf.setFillColor(WHITE)
        pdf.setFont("Helvetica-Bold", 9)
        pdf.drawCentredString(width - 55*mm, y - 13*mm, "APPROVED")

        # ── Section: Important Instructions ──
        y -= box_h + 12*mm
        pdf.setFillColor(PRIMARY)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(25*mm, y, "IMPORTANT INSTRUCTIONS")
        y -= 2*mm
        pdf.setStrokeColor(PRIMARY)
        pdf.setLineWidth(0.8)
        pdf.line(25*mm, y, width - 25*mm, y)

        instructions = [
            "Please arrive 15 minutes before your scheduled appointment time.",
            "Carry a valid government-issued photo ID (Aadhar card preferred).",
            "Bring this appointment confirmation (printed or digital copy).",
            "Inform the hospital staff if you have any pre-existing medical conditions.",
            "Contact the hospital if you need to reschedule or cancel.",
        ]

        y -= 6*mm
        pdf.setFillColor(DARK)
        pdf.setFont("Helvetica", 8.5)
        for instruction in instructions:
            pdf.drawString(28*mm, y, f"•   {instruction}")
            y -= 5.5*mm

        # ── Footer ──
        footer_y = 25*mm
        pdf.setStrokeColor(GREY)
        pdf.setLineWidth(0.5)
        pdf.line(25*mm, footer_y + 8*mm, width - 25*mm, footer_y + 8*mm)

        pdf.setFillColor(GREY)
        pdf.setFont("Helvetica", 7)
        pdf.drawString(25*mm, footer_y + 3*mm,
                       f"Generated on {datetime.now().strftime('%d %B %Y, %I:%M %p')}  |  MediFlow — Blood & Organ Donation Finder Platform")
        pdf.drawString(25*mm, footer_y - 1*mm,
                       "This is a system-generated document. No signature is required. For queries, contact the issuing hospital.")

        pdf.showPage()
        pdf.save()
        # ── End PDF Generation ───────────────────────────────────────

        application.appointment_pdf = f"appointments/{filename}"
        application.save()

        return JsonResponse({'success': True})
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