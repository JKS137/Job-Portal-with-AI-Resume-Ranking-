from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    ApplicationViewSet,
    HealthCheckView,
    JobPostingViewSet,
    RegisterView,
    ResumeViewSet,
)

router = DefaultRouter()
router.register('jobs', JobPostingViewSet, basename='job')
router.register('resumes', ResumeViewSet, basename='resume')
router.register('applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
