from rest_framework.viewsets import ModelViewSet
from core.permissions import IsCompanyAuthOrReadOnly, IsJobPostOwnerOrReadOnly

from core.models import Job
from core.serializers import (
    JobSerializer,
    JobCreateSerializer,
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
