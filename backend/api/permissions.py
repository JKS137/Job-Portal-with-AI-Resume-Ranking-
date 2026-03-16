from rest_framework.permissions import BasePermission


class IsRecruiter(BasePermission):
    """Allow access only to users with recruiter role."""

    def has_permission(self, request, view):
        return getattr(getattr(request.user, 'profile', None), 'role', None) == 'recruiter'


class IsOwnerOrReadOnly(BasePermission):
    """Allow owners to edit, others can read."""

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj == getattr(request.user, 'profile', None) or obj == request.user
