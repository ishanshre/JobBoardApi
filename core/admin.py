from django.contrib import admin

# Register your models here.
from core.models import Job, JobApply


admin.site.register(Job)
admin.site.register(JobApply)