from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from authentication.serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
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


class UserLoginApiView(GenericAPIView):
    serializer_class = UserLoginSerializer
    http_method_names = ['post','options','head']
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutApiView(GenericAPIView):
    serializer_class = UserLogoutSerializer
    http_method_names = ['post','options','head']
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success":"Logout Successfull",
        }, status=status.HTTP_200_OK)