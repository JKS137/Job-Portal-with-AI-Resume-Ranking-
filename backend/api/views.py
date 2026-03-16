from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Application, JobPosting, Resume
from .permissions import IsRecruiter
from .serializers import (
    ApplicationCreateSerializer,
    ApplicationSerializer,
    JobPostingSerializer,
    RegisterSerializer,
    ResumeSerializer,
    UserSerializer,
)


from rest_framework.views import APIView


class HealthCheckView(APIView):
    """Simple health check endpoint."""

    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'status': 'ok'})


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all().order_by('-posted_at')
    serializer_class = JobPostingSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsRecruiter()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all().order_by('-uploaded_at')
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('-submitted_at')
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if getattr(getattr(user, 'profile', None), 'role', None) == 'recruiter':
            return self.queryset.filter(job__recruiter=user)
        return self.queryset.filter(candidate=user)

    def get_serializer_class(self):
        if self.action == 'create':
            return ApplicationCreateSerializer
        return ApplicationSerializer

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)
