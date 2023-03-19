from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ViewSet

from .serializers import ProductSerializers, ProductFavoriteSerializer, ProductCategory
from .permissions import IsOwnerAccOrAdmin

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from product_module.models import Products, ProductFavorite, Category


class ProductListView(APIView):
    permission_classes = [permissions.AllowAny, ]
    serializer = ProductSerializers
    data = Products.objects.filter(is_available=True)

    def get(self, request, *args, **kwargs):
        final_data = self.data
        size = request.GET.get('size')
        if size:
            final_data = final_data.filter(size__size__iexact=size)
        category = request.GET.get('category')
        if category:
            final_data = final_data.filter(category__iexact=category)
        color = request.GET.get('color')
        if color:
            final_data = final_data.filter(color__iexact=color)
        brand = request.GET.get('brand')
        if brand:
            final_data = final_data.filter(brand__name__iexact=brand)
        srz_data = self.serializer(instance=final_data, many=True).data
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


class ProductFavoriteView(APIView):
    # todo: custom perm
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ProductFavoriteSerializer

    def get(self, request, pk=None):
        data = ProductFavorite.objects.all()
        if pk:
            user = get_object_or_404(User, pk=pk)
            data = data.filter(user_id=user.id)
        srz_data = ProductFavoriteSerializer(instance=data, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)


class ProductCategoryView(ViewSet):
    """
    CRUD for products category
    """

    queryset = Category.objects.filter(is_available=True)

    def get_permissions(self):
        if self.action == 'list' or 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request):
        srz_data = ProductCategory(instance=self.queryset, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        data = get_object_or_404(self.queryset, pk=pk)
        srz_data = ProductCategory(instance=data).data
        return Response(data=srz_data, status=status.HTTP_200_OK)

    def create(self, request):
        srz_data = ProductCategory(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        data = get_object_or_404(self.queryset, pk=pk)
        srz_data = ProductCategory(instance=data, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = get_object_or_404(self.queryset, pk=pk)
        data.is_available = False
        data.save()
        return Response(data={'SUCCESSFULLY': 'Deactivated'})