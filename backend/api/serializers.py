from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Application, JobPosting, Profile, Resume


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'role']

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, role=role)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'role']
        read_only_fields = ['id']


class ResumeSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Resume
        fields = ['id', 'owner', 'file', 'uploaded_at']
        read_only_fields = ['id', 'owner', 'uploaded_at']


class JobPostingSerializer(serializers.ModelSerializer):
    recruiter = UserSerializer(read_only=True)

    class Meta:
        model = JobPosting
        fields = [
            'id',
            'title',
            'company_name',
            'location',
            'employment_type',
            'description',
            'requirements',
            'posted_at',
            'recruiter',
        ]
        read_only_fields = ['id', 'posted_at', 'recruiter']


class ApplicationSerializer(serializers.ModelSerializer):
    candidate = UserSerializer(read_only=True)
    job = JobPostingSerializer(read_only=True)
    resume = ResumeSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            'id',
            'job',
            'candidate',
            'resume',
            'status',
            'submitted_at',
        ]
        read_only_fields = ['id', 'candidate', 'submitted_at']


class ApplicationCreateSerializer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(queryset=JobPosting.objects.all())
    resume = serializers.PrimaryKeyRelatedField(queryset=Resume.objects.all())

    class Meta:
        model = Application
        fields = ['job', 'resume']
