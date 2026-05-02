from django.shortcuts import render,redirect
from home.models import OrganDonation,BloodDonation,BloodRequest,OrganRequest,EmergencyBloodRequest,EmergencyOrganRequest,HospitalNews,EmergencyNotification
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.conf import settings
import os


# Create your views here.
@login_required(login_url="users:login_user")
def user_dashboard(request):
    news_list = HospitalNews.objects.all().order_by("-created_at")
    user = request.user

    notifications = EmergencyNotification.objects.filter(donor=request.user).filter( Q(blood_request__is_active=True) | Q(organ_request__is_active=True))

    context = {
        "blood_donations": BloodDonation.objects.filter(user=user).order_by("-approved_at"),
        "organ_donations": OrganDonation.objects.filter(user=user).order_by("-approved_at"),
        "blood_requests": BloodRequest.objects.filter(user=user).order_by("-approved_at"),
        "organ_requests": OrganRequest.objects.filter(user=user).order_by("-approved_at"),
        "emergency_blood_requests": EmergencyBloodRequest.objects.filter(user=user).order_by("-approved_at"),
        "emergency_organ_requests": EmergencyOrganRequest.objects.filter(user=user).order_by("-approved_at"),
        "news_list": news_list,
        "notifications":notifications,
    }
    
    return render(request, "user_dashboard.html", context)

def emergency_status(request):
    form_id   = request.session.get("emergency_form_id")
    req_type  = request.session.get("emergency_req_type", "blood")
    req_phone = request.session.get("emergency_req_phone", "")

    if not form_id:
        # Someone landed here without a valid session — send them to the form
        return redirect("emergency_request")

    # Fetch the actual request object to pass initial data to the template
    if req_type == "blood":
        try:
            req_obj = EmergencyBloodRequest.objects.get(form_id=form_id)
        except EmergencyBloodRequest.DoesNotExist:
            return redirect("emergency_request")
        need_label = f"{req_obj.blood_group} Blood"
    else:
        try:
            req_obj = EmergencyOrganRequest.objects.get(form_id=form_id)
        except EmergencyOrganRequest.DoesNotExist:
            return redirect("emergency_request")
        need_label = req_obj.organ
     # Resolve donor details safely in Python, not in the template
    already_found = (not req_obj.is_active) and bool(req_obj.accepted_donor_id)
    donor_name  = ""
    donor_phone = ""
    donor_city  = ""

    if already_found:
        try:
            profile     = req_obj.accepted_donor.userprofile
            donor_name  = profile.full_name
            donor_phone = profile.phone
            donor_city  = profile.city or "—"
        except Exception:
            donor_name  = req_obj.accepted_donor.username
            donor_phone = "—"
            donor_city  = "—"

    context = {
    "already_found": already_found,
    "form_id": form_id,
    "req_type": req_type,
    "req_phone": req_phone,
    "need_label": need_label,
    "city": req_obj.city,
    "is_active": req_obj.is_active,
    "donor_name": donor_name,
    "donor_phone": donor_phone,
    "donor_city": donor_city,
}
    return render(request, "emergency_status.html", context)


def check_emergency_status(request):
    form_id  = request.GET.get("form_id")
    req_type = request.GET.get("req_type", "blood")

    if not form_id:
        return JsonResponse({"found": False})

    if req_type == "blood":
        try:
            obj = EmergencyBloodRequest.objects.get(form_id=form_id)
        except EmergencyBloodRequest.DoesNotExist:
            return JsonResponse({"found": False})
    else:
        try:
            obj = EmergencyOrganRequest.objects.get(form_id=form_id)
        except EmergencyOrganRequest.DoesNotExist:
            return JsonResponse({"found": False})

    if obj.accepted_donor:
        # Expose only safe contact info
        try:
            donor_profile = obj.accepted_donor.userprofile
            donor_name    = donor_profile.full_name
            donor_phone   = donor_profile.phone
            donor_city    = donor_profile.city or "—"
        except Exception:
            donor_name  = obj.accepted_donor.get_full_name() or obj.accepted_donor.username
            donor_phone = "—"
            donor_city  = "—"

        return JsonResponse({
            "found"      : True,
            "donor_name" : donor_name,
            "donor_phone": donor_phone,
            "donor_city" : donor_city,
        })

    return JsonResponse({"found": False})

@login_required
@require_POST
def accept_emergency(request):

    notif_id = request.POST.get("notification_id")

    try:
        notification = EmergencyNotification.objects.select_related(
            "blood_request", "organ_request"
        ).get(id=notif_id, donor=request.user)
    except EmergencyNotification.DoesNotExist:
        return redirect("user_dashboard")

    if notification.blood_request:
        req = notification.blood_request

    else:
        req = notification.organ_request

    if not req.is_active:
        return redirect("user_dashboard")

    req.accepted_donor = request.user
    req.status = "approved"
    req.is_active = False
    req.save()

    if notification.blood_request:
        req = notification.blood_request
        EmergencyNotification.objects.filter(blood_request=req).delete()

    elif notification.organ_request:
        req = notification.organ_request
        EmergencyNotification.objects.filter(organ_request=req).delete()

    return redirect("user_dashboard")

@login_required(login_url="users:login_user")
@require_POST
def clear_application(request):
    """Delete a user's application completely."""
    app_type = request.POST.get('app_type')
    form_id = request.POST.get('form_id')

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
        application = model_map[app_type].objects.get(form_id=form_id, user=request.user)
    except model_map[app_type].DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Application not found'})

    # Delete associated PDF file from disk
    if hasattr(application, 'appointment_pdf') and application.appointment_pdf:
        pdf_path = os.path.join(settings.MEDIA_ROOT, str(application.appointment_pdf))
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    # Delete the doc_report file too if it exists
    if hasattr(application, 'doc_report') and application.doc_report:
        report_path = os.path.join(settings.MEDIA_ROOT, str(application.doc_report))
        if os.path.exists(report_path):
            os.remove(report_path)

    application.delete()
    return JsonResponse({'success': True})
