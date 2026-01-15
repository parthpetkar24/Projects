from django.contrib import admin
from .models import UserProfile,HospitalProfile,BloodDonation,OrganDonation,BloodRequest,OrganRequest,EmergencyBloodRequest,EmergencyOrganRequest

admin.site.register(UserProfile)
admin.site.register(HospitalProfile)
admin.site.register(BloodDonation)
admin.site.register(OrganDonation)
admin.site.register(BloodRequest)
admin.site.register(OrganRequest)
admin.site.register(EmergencyBloodRequest)
admin.site.register(EmergencyOrganRequest)
