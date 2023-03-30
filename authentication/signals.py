from django.dispatch import receiver

from django.db.models.signals import post_save

from django.contrib.auth import get_user_model

from authentication.models import CompanyProfile, JobSeekerProfile

User = get_user_model()

@receiver(signal=post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_company:
            company = CompanyProfile.objects.create(user=instance)
            company.save()
        elif instance.is_job_seeker:
            job = JobSeekerProfile.objects.create(user=instance)
            job.save()