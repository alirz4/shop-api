from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(upload_to='media/products', verbose_name='Image', null=True, blank=True)
    price = models.IntegerField(verbose_name='Price')
    off_price = models.IntegerField(verbose_name='OFF price', validators=[MinValueValidator(1), MaxValueValidator(100)],
                                    null=True, blank=True)
    category = models.ManyToManyField('Category', blank=True)
    # image_list = models.ManyToManyField('ProductImages', verbose_name='Gallery', related_name='product')
    # sizes = models.ManyToManyField('ProductSize', verbose_name='Size', related_name='product')
    color = models.CharField(max_length=30, verbose_name='Color')
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    SIZE = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('2XL', '2XL'),
    )
    size = models.CharField(max_length=10, verbose_name='Size', choices=SIZE)
    stoke = models.IntegerField(validators=[MinValueValidator(0), ], verbose_name='Stoke')

    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='size', verbose_name='Product')

    def __str__(self):
        return f'{self.size} - {self.stoke}'


class ProductImages(models.Model):
    image = models.ImageField(upload_to='products/gallery', verbose_name='Image')

    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='gallery', verbose_name='Product')

    def __str__(self):
        return self.product.name


class ProductDescription(models.Model):
    description = models.TextField()
    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='desc')

    def __str__(self):
        return f'{self.product.name} - {self.description[:15]}'
