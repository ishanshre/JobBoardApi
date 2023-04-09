from rest_framework import serializers

from core.models import Job, JobApply
from authentication.serializers import UserCompanyProfileSerializer, UserJobSeekerProfileSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class JobSerializer(serializers.ModelSerializer):
    created_by = UserCompanyProfileSerializer(read_only=True)
    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'description',
            'currency',
            'minmum_wage',
            'maximum_wage',
            'no_of_vacancy',
            'deadline',
            'position_time',
            'work_location',
            'level',
            'experince',
            'prefered_age',
            'education',
            'created_by',
            'created_at',
            'updated_at'
        ]
class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'title',
            'description',
            'currency',
            'minmum_wage',
            'maximum_wage',
            'no_of_vacancy',
            'deadline',
            'position_time',
            'work_location',
            'level',
            'experince',
            'prefered_age',
            'education',
        ]
    
    def create(self, validated_data):
        created_by = self.context['user']
        job = Job.objects.create(**validated_data,created_by=created_by)
        job.save()
        return job


class JobApplySerializer(serializers.ModelSerializer):
    applied_by = UserJobSeekerProfileSerializer()
    class Meta:
        model = JobApply
        fields = ['id','applied_job','applied_by','cover_letter','resume','certificates']


class JobApplyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApply
        fields = ['cover_letter','resume','certificates']
    
    def create(self, validated_data):
        user = self.context['user']
        applied_job = self.context['applied_job']
        job_apply = JobApply(**validated_data)
        job_apply.applied_by = user
        job_apply.applied_job = applied_job
        job_apply.save()
        return job_apply