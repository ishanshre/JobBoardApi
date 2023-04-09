from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsCompanyAuthOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and 
            request.user.is_authenticated and 
            request.user.is_company)
        )


class IsCompanyAuth(BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and request.user.is_company)


class IsJobPostOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user


class IsJobSeekerAuthOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_job_seeker
        )

class IsJobSeekerAuth(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_job_seeker
        )


class IsJobAppliedByJobSeekerAuth(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user and request.user.is_authenticated and obj.applied_by == request.user)

