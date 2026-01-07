from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=122)
    phone=models.CharField(max_length=15)
    blood_group = models.CharField(
        max_length=3,
        choices=[
            ('A+', 'A+'), ('A-', 'A-'),
            ('B+', 'B+'), ('B-', 'B-'),
            ('AB+', 'AB+'), ('AB-', 'AB-'),
            ('O+', 'O+'), ('O-', 'O-'),
        ],
        null=True,
        blank=True
    )
    city = models.CharField(max_length=60, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.full_name
    
class HospitalProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    hospital_name=models.CharField(max_length=122)
    registration_id=models.CharField(max_length=122)
    city=models.CharField(max_length=60)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    contact_number=models.CharField(max_length=15)
    license=models.FileField(
        upload_to="hospital_licenses/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.hospital_name