from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

User = get_user_model()

class Job(models.Model):
    class TIME_TYPE(models.TextChoices):
        FULL = "Full Time", 'Full Time'
        PART = "Part Time", 'Part Time'
    

    class LOCATION_TYPE(models.TextChoices):
        REMOTE = "Remote Location", 'Remote Location'
        OFFICE = "Office Location", 'Office Location'

    class LEVEL_TYPE(models.TextChoices):
        ENTRY = "Entry", 'Entry Level'
        INTERMEDIATE = 'Intermediate', 'Intermediate Level'
        SENIOR = "Senior", 'Senior Level'

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs_created")
    title = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    minmum_wage = models.PositiveBigIntegerField()
    maximum_wage = models.PositiveBigIntegerField()
    no_of_vacancy = models.PositiveIntegerField()
    deadline = models.DateField()
    description = models.TextField()
    position_time = models.CharField(max_length=9, choices=TIME_TYPE.choices, default=TIME_TYPE.FULL)
    work_location = models.CharField(max_length=15, choices=LOCATION_TYPE.choices, default=LOCATION_TYPE.OFFICE)
    level = models.CharField(max_length=12, choices=LEVEL_TYPE.choices, default=LEVEL_TYPE.ENTRY)
    education = models.CharField(max_length=255)
    experince = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)])
    prefered_age = models.PositiveBigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobApply(models.Model):
    applied_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs_applied")
    applied_job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_seekers')
    cover_letter = models.FileField(upload_to="user/coverLetter")
    resume = models.FileField(upload_to="user/resume")
    certificates = models.FileField(upload_to="user/certificates", blank=True, null=True)

    def __str__(self):
        return self.applied_by.username