from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers import (
    UserRegisterSerializer
)

class UserRegisterApiView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    http_method_names = ['post','options','head']
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success":serializer.data,
        }, status=status.HTTP_201_CREATED)