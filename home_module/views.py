from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from home_module.serializers import UserSerializer


class UserView(APIView):
    data = User.objects.all()

    def get(self, request):
        srz_data = UserSerializer(instance=self.data, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)
