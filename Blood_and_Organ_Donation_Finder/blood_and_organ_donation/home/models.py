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
    weight=models.PositiveIntegerField()
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

    def __str__(self):
        return self.form_id

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
    weight=models.PositiveIntegerField()
    medical_condition=models.CharField(max_length=122)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True,null=True, blank=True)

    def __str__(self):
        return self.form_id
    
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
    weight=models.PositiveIntegerField()
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

    def __str__(self):
        return self.form_id
    
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
    weight=models.PositiveIntegerField()
    medical_condition=models.CharField(max_length=122)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True,null=True, blank=True)

    def __str__(self):
        return self.form_id
    
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
    weight=models.PositiveIntegerField()
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

    def __str__(self):
        return self.form_id

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
    weight=models.PositiveIntegerField()
    medical_condition=models.CharField(max_length=122)
    doc_report=models.FileField(
        upload_to='user_report/',
        null=True,
        blank=True
    )
    form_id=models.CharField(max_length=5,unique=True,null=True, blank=True)

    def __str__(self):
        return self.form_id