from django.contrib import admin
from .models import UserProfile,HospitalProfile,BloodDonation,OrganDonation

admin.site.register(UserProfile)
admin.site.register(HospitalProfile)
admin.site.register(BloodDonation)
admin.site.register(OrganDonation)
