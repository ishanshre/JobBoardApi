from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class JobApplierInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField()
    cover_letter = models.FileField(upload_to="user/coverLetter")
    resume = models.FileField(upload_to="user/resume")
    certificates = models.FileField(upload_to="user/certificates", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_appliers_archives")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"job applied info -{self.email}- to company {self.created_by.company_profile.company_name}"