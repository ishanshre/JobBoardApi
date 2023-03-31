from rest_framework import serializers
from rest_framework.settings import api_settings

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError

from authentication.models import CompanyProfile, JobSeekerProfile

User = get_user_model()

class UserInfoSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)
    confirm_password = serializers.CharField(max_length=255, write_only=True)
    is_company = serializers.BooleanField(default=False)
    is_job_seeker = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password','is_company','is_job_seeker']
    
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if len(username) < 6:
            raise serializers.ValidationError({
                "error":"username must be of length more than 5 characters"
            })
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({
                "error":f"username: {username} already exists"
            })
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                "error":f"email: {email} already exists"
            })
        
        user = User(username=username, email=email)
        try:
            validate_password(user=user, password=password)
        except ValidationError as e:
            serializers_errors = serializers.as_serializer_error(e)
            raise serializers.ValidationError({
                "error":serializers_errors[api_settings.NON_FIELD_ERRORS_KEY]
            })
        if password != confirm_password:
            raise serializers.ValidationError({
                "error":"passwords does not match"
            })
        return attrs

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        is_company = validated_data['is_company']
        is_job_seeker = validated_data['is_job_seeker']
        user = User.objects.create_user(
            username=username,
            email=email,
            is_company=is_company,
            is_job_seeker=is_job_seeker
        )
        user.set_password(validated_data['password'])
        user.save()
        return user