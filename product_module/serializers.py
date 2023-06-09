from rest_framework import serializers

from product_module.models import Products, ProductSize, ProductImages, ProductDescription, ProductFavorite, Category, \
    ProductBrands


class ProductSerializers(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    specification = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = '__all__'

    def get_sizes(self, obj):
        result = obj.size.all()
        return ProductSizeSerializer(instance=result, many=True).data

    def get_images(self, obj):
        result = obj.gallery.all()
        return ProductImagesSerializer(instance=result, many=True).data

    def get_specification(self, obj):
        result = obj.desc.all()
        return ProductDescSerializer(instance=result, many=True).data


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        # fields = '__all__'
        exclude = ['id', 'product']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        # fields = '__all__'
        exclude = ['id', 'product']


class ProductDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescription
        # fields = '__all__'
        exclude = ['id', 'product']


class ProductCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFavorite
        exclude = ['id', ]


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrands
        fields = '__all__'
