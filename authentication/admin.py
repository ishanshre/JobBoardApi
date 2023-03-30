from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from authentication.forms import CustomUserChangeForm, CustomUserCreationForm
from authentication.models import CompanyProfile, JobSeekerProfile
# Register your models here.

User = get_user_model()

class CompanyProfileInline(admin.StackedInline):
    model=CompanyProfile

class JobSeekerProfileInline(admin.StackedInline):
    model = JobSeekerProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username','is_staff','is_company','is_job_seeker','email_confirmed']
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = BaseUserAdmin.fieldsets + (
        ("None", {
            "fields":("is_company",'is_job_seeker','email_confirmed'),
        }),
    )
    add_fieldsets = (
        ("Create User", {
            "classes":("wide"),
            "fields":("username","email",'password1','password2', 'is_company','is_job_seeker'),
        }),
    )

    def get_inlines(self, request, obj=None):
        if obj:
            if obj.is_company:
                return [CompanyProfileInline]
            elif obj.is_job_seeker:
                return [JobSeekerProfileInline]
        return []