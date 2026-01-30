from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
]


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
    )
    city = models.CharField(max_length=60, null=True)
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
    aplusunit=models.IntegerField(default=0)
    aminusunit=models.IntegerField(default=0)
    bplusunit=models.IntegerField(default=0)
    bminusunit=models.IntegerField(default=0)
    abplusunit=models.IntegerField(default=0)
    abminusunit=models.IntegerField(default=0)
    oplusunit=models.IntegerField(default=0)
    ominusunit=models.IntegerField(default=0)
    def __str__(self):
        return self.hospital_name
    
class BloodDonation(models.Model):
    full_name=models.CharField(max_length=122)
    aadhar_id=models.CharField(max_length=12)
    dob=models.DateField()
    gender=models.CharField(
        max_length=15,
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            ('PNS','Prefer Not Say'),
        ],
        null=True
    )
    city=models.CharField(max_length=60)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
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
    )
    weight=models.FloatField()
    medical_condition=models.CharField(
        max_length=122,
        blank=True,
        null=True)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    approved_by = models.ForeignKey(
        HospitalProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_blood_donations'
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.status == 'approved' and self.approved_at is None:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.form_id or f"BloodDonation #{self.pk}"

class OrganDonation(models.Model):
    full_name=models.CharField(max_length=122)
    aadhar_id=models.CharField(max_length=12)
    dob=models.DateField()
    gender=models.CharField(
        max_length=15,
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            ('PNS','Prefer Not Say'),
        ],
        null=True
    )
    city=models.CharField(max_length=60)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    phone=models.CharField(max_length=15)
    aliveordec=models.CharField(
        max_length=10,
        choices=[
            ("A","Alive"),
            ("D","Deceased")
        ],
        null=True
    )
    organ = models.CharField(
        max_length=20,
        choices=[
            ('Kidney', 'Kidney'), 
            ('Liver', 'Liver'),
            ('Lungs', 'Lungs'), 
            ('Heart', 'Heart'),
            ('Pancreas', 'Pancreas'), 
            ('Intestine', 'Intestine'),
            ('Uterus', 'Uterus'), 
            ('Eyes', 'Eyes'),
            ('Tissues','Tissues'),
        ],
        null=True,
    )
    weight=models.FloatField()
    medical_condition=models.CharField(max_length=122)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True,null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    approved_by = models.ForeignKey(
        HospitalProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_organ_donations'
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.status == 'approved' and self.approved_at is None:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.form_id or f"OrganDonation #{self.pk}"
    
class BloodRequest(models.Model):
    full_name=models.CharField(max_length=122)
    aadhar_id=models.CharField(max_length=12)
    dob=models.DateField()
    gender=models.CharField(
        max_length=15,
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            ('PNS','Prefer Not Say'),
        ],
        null=True
    )
    city=models.CharField(max_length=60)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
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
    )
    weight=models.FloatField()
    medical_condition=models.CharField(
        max_length=122,
        blank=True,
        null=True)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    approved_by = models.ForeignKey(
        HospitalProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_blood_requests'
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.status == 'approved' and self.approved_at is None:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.form_id or f"BloodRequest #{self.pk}"
    
class OrganRequest(models.Model):
    full_name=models.CharField(max_length=122)
    aadhar_id=models.CharField(max_length=12)
    dob=models.DateField()
    gender=models.CharField(
        max_length=15,
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            ('PNS','Prefer Not Say'),
        ],
        null=True
    )
    city=models.CharField(max_length=60)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    phone=models.CharField(max_length=15)
    organ = models.CharField(
        max_length=20,
        choices=[
            ('Kidney', 'Kidney'), 
            ('Liver', 'Liver'),
            ('Lungs', 'Lungs'), 
            ('Heart', 'Heart'),
            ('Pancreas', 'Pancreas'), 
            ('Intestine', 'Intestine'),
            ('Uterus', 'Uterus'), 
            ('Eyes', 'Eyes'),
            ('Tissues','Tissues'),
        ],
        null=True,
    )
    weight=models.FloatField()
    medical_condition=models.CharField(max_length=122)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True,null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    approved_by = models.ForeignKey(
        HospitalProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_organ_requests'
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.status == 'approved' and self.approved_at is None:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.form_id or f"OrganRequest #{self.pk}"
    
class EmergencyBloodRequest(models.Model):
    full_name=models.CharField(max_length=122)
    aadhar_id=models.CharField(max_length=12)
    dob=models.DateField()
    gender=models.CharField(
        max_length=15,
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            ('PNS','Prefer Not Say'),
        ],
        null=True
    )
    city=models.CharField(max_length=60)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
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
    )
    weight=models.FloatField()
    medical_condition=models.CharField(
        max_length=122,
        blank=True,
        null=True)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    approved_by = models.ForeignKey(
        HospitalProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_emergency_blood_requests'
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.status == 'approved' and self.approved_at is None:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.form_id or f"EmergencyBloodRequest #{self.pk}"

class EmergencyOrganRequest(models.Model):
    full_name=models.CharField(max_length=122)
    aadhar_id=models.CharField(max_length=12)
    dob=models.DateField()
    gender=models.CharField(
        max_length=15,
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            ('PNS','Prefer Not Say'),
        ],
        null=True
    )
    city=models.CharField(max_length=60)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    phone=models.CharField(max_length=15)
    organ = models.CharField(
        max_length=20,
        choices=[
            ('Kidney', 'Kidney'), 
            ('Liver', 'Liver'),
            ('Lungs', 'Lungs'), 
            ('Heart', 'Heart'),
            ('Pancreas', 'Pancreas'), 
            ('Intestine', 'Intestine'),
            ('Uterus', 'Uterus'), 
            ('Eyes', 'Eyes'),
            ('Tissues','Tissues'),
        ],
        null=True,
    )
    weight=models.FloatField()
    medical_condition=models.CharField(max_length=122)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True,null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    approved_by = models.ForeignKey(
        HospitalProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_emergency_organ_requests'
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.status == 'approved' and self.approved_at is None:
            self.approved_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.form_id or f"EmergencyOrganRequest #{self.pk}"
