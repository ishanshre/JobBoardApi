from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.permissions import (
    IsCompanyAuthOrReadOnly,
    IsJobPostOwnerOrReadOnly,
    IsCompanyAuth,
    IsJobSeekerAuth,
)
from core.models import Job, JobApply
from core.serializers import (
    JobSerializer,
    JobListSerializer,
    JobCreateSerializer,
    JobApplySerializer,
    JobApplyCreateSerializer,
)

class JobModelViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def get_permissions(self):
        if self.request.method in ('PUT','PATCH', 'DELETE'):
            return [IsCompanyAuthOrReadOnly(), IsJobPostOwnerOrReadOnly()] 
        return [IsCompanyAuthOrReadOnly()]


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return JobCreateSerializer
        return JobSerializer
    
    def get_serializer_context(self):
        return {
            "user":self.request.user
        }
    
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = JobListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class JobApplyModelViewSet(ModelViewSet):
    http_method_names = ['get','post','delete','options','head']
    serializer_class = JobApplySerializer
    queryset = JobApply.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsJobSeekerAuth()]
        if self.request.method in ("GET", "DELETE"):
            return [IsCompanyAuth()]
        return [IsAuthenticated()]

    def get_serializer_context(self):
        applied_job = Job.objects.get(pk=self.kwargs['job_pk'])
        return {
            'user': self.request.user,
            "applied_job":applied_job
        }

    def get_serializer_class(self):
        if self.request.method == "POST":
            return JobApplyCreateSerializer
        return JobApplySerializer