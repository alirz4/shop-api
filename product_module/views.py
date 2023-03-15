from django.shortcuts import render, get_object_or_404

from .serializers import ProductSerializers

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from product_module.models import Products


class ProductListView(APIView):
    permission_classes = [permissions.AllowAny, ]
    serializer = ProductSerializers
    data = Products.objects.filter(is_available=True)

    def get(self, request):
        srz_data = self.serializer(instance=self.data, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    serializer = ProductSerializers
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, pk):
        data = get_object_or_404(Products, pk=pk)
        srz_data = self.serializer(instance=data).data
        return Response(data=srz_data, status=status.HTTP_200_OK)


class ProductEditView(APIView):
    serializer = ProductSerializers
    permission_classes = [permissions.IsAdminUser, ]

    def put(self, request, pk):
        data = get_object_or_404(Products, pk=pk)
        srz_data = self.serializer(instance=data, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCreateView(APIView):
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = ProductSerializers

    def post(self, request):
        srz_data = ProductSerializers(data=request.data)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAdminUser, ]

    def delete(self, request, pk):
        data = get_object_or_404(Products, pk=pk)
        data.is_available = False
        data.save()
        return Response({"successfully": 'disabled'}, status=status.HTTP_200_OK)