from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField

from authentication.sector import SECTOR_SELECT, COMPANY_TYPE
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    is_company = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)


class Profile(models.Model):
    description = models.TextField(max_length=15000, blank=True)
    address = models.CharField(max_length=500, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    tax_id = models.PositiveBigIntegerField(null=True,blank=True)
    instagram = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True

class CompanyProfile(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=255)
    sector = models.CharField(max_length=40, choices=SECTOR_SELECT.choices, null=True, blank=True)
    type = models.CharField(max_length=30, choices=COMPANY_TYPE.choices, null=True, blank=True)
    registeration_no = models.PositiveBigIntegerField(null=True, blank=True)
    pan = models.ImageField(upload_to="user/company/pan", null=True, blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    size = models.PositiveIntegerField(null=True, blank=True)
    date_of_establishment = models.DateField(null=True, blank=True)
    logo = models.ImageField(upload_to="user/company/logo", null=True, blank=True)

    def __str__(self):
        return self.company_name
    


class JobSeekerProfile(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile')
    profile_pic = models.ImageField(upload_to="user/jobseeker/profile/", null=True, blank=True)
    citizenship = models.ImageField(upload_to="user/jobseeker/identity", null=True, blank=True)
    passport = models.ImageField(upload_to="user/jobseeker/identity", null=True, blank=True)
    driving_license = models.ImageField(upload_to="user/jobseeker/identity", null=True, blank=True)
    cover_letter = models.FileField(upload_to="user/jobseeker/resume", null=True, blank=True)
    resume = models.FileField(upload_to="user/jobseeker/resume", null=True, blank=True)
    
    def __str__(self):
        return self.user.username