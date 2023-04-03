from rest_framework import serializers

from core.models import Job

from authentication.serializers import UserCompanyProfileSerializer

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
