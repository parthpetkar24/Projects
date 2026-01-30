from django.contrib import admin
from .models import UserProfile, HospitalProfile, BloodDonation, OrganDonation, BloodRequest, OrganRequest, EmergencyBloodRequest, EmergencyOrganRequest


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'blood_group', 'city')
    search_fields = ('full_name', 'phone', 'city')
    list_filter = ('blood_group', 'city')

@admin.register(HospitalProfile)
class HospitalProfileAdmin(admin.ModelAdmin):
    list_display = ('hospital_name', 'registration_id', 'city', 'contact_number')
    search_fields = ('hospital_name', 'registration_id', 'city')
    list_filter = ('city',)

@admin.register(BloodDonation)
class BloodDonationAdmin(admin.ModelAdmin):
    list_display = (
        'form_id', 'full_name', 'blood_group',
        'city', 'status', 'approved_by', 'approved_at'
    )
    list_filter = ('status', 'blood_group', 'city')
    search_fields = ('form_id', 'full_name', 'phone', 'aadhar_id')
    readonly_fields = ('approved_at',)

@admin.register(OrganDonation)
class OrganDonationAdmin(admin.ModelAdmin):
    list_display = (
        'form_id', 'full_name', 'organ',
        'city', 'status', 'approved_by', 'approved_at'
    )
    list_filter = ('status', 'organ', 'city')
    search_fields = ('form_id', 'full_name', 'phone', 'aadhar_id')
    readonly_fields = ('approved_at',)

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = (
        'form_id', 'full_name', 'blood_group',
        'city', 'status', 'approved_by', 'approved_at'
    )
    list_filter = ('status', 'blood_group', 'city')
    search_fields = ('form_id', 'full_name', 'phone', 'aadhar_id')
    readonly_fields = ('approved_at',)

@admin.register(OrganRequest)
class OrganRequestAdmin(admin.ModelAdmin):
    list_display = (
        'form_id', 'full_name', 'organ',
        'city', 'status', 'approved_by', 'approved_at'
    )
    list_filter = ('status', 'organ', 'city')
    search_fields = ('form_id', 'full_name', 'phone', 'aadhar_id')
    readonly_fields = ('approved_at',)

@admin.register(EmergencyBloodRequest)
class EmergencyBloodRequestAdmin(admin.ModelAdmin):
    list_display = (
        'form_id', 'full_name', 'blood_group',
        'city','approved_by', 'approved_at'
    )
    list_filter = ('status','blood_group', 'city')
    search_fields = ('form_id', 'full_name', 'phone', 'aadhar_id')
    readonly_fields = ('approved_at',)

@admin.register(EmergencyOrganRequest)
class EmergencyOrganRequestAdmin(admin.ModelAdmin):
    list_display = (
        'form_id', 'full_name', 'organ',
        'city','approved_by', 'approved_at'
    )
    list_filter = ('status','organ', 'city')
    search_fields = ('form_id', 'full_name', 'phone', 'aadhar_id')
    readonly_fields = ('approved_at',)