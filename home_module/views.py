from django.shortcuts import render

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from home_module.serializers import UserSerializer, UserRegisterSerializer


class UserView(APIView):
    permission_classes =  [permissions.IsAdminUser, ]
    data = User.objects.all()

    def get(self, request):
        srz_data = UserSerializer(instance=self.data, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.data)
        if srz_data.is_valid():
            cd = srz_data.validated_data
            User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

