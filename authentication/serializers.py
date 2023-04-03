from rest_framework import serializers
from rest_framework.settings import api_settings

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import update_last_login

from django.core.exceptions import ValidationError

from authentication.models import CompanyProfile, JobSeekerProfile

User = get_user_model()

class UserInfoSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ['id', 'title', 'logo', 'sector', 'type', 'latitude', 'longitude']


class UserCompanyProfileSerializer(serializers.ModelSerializer):
    profile = CompanyProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','profile']


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
    


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    access_token = serializers.CharField(max_length=500, read_only=True)
    refresh_token = serializers.CharField(max_length=500, read_only=True)
    class Meta:
        model = User
        fields = ['id','username','password', 'access_token','refresh_token']
        

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({
                "error":"invalid username/password"
            })
        if not user.is_active:
            raise serializers.ValidationError({
                "error":"user is not active"
            })
        token = user.get_tokens()
        update_last_login(None, user=user)
        attrs['id'] = user.id
        attrs['access_token'] = token['access']
        attrs['refresh_token'] = token['refresh']
        return attrs


class UserLogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs.get("refresh_token")
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError({
                "error":"Invalid/Bad Token"
            })
        
        