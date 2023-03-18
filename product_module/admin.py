from django.contrib import admin
from . import models

admin.site.register(models.Products)
admin.site.register(models.Category)
admin.site.register(models.ProductImages)
admin.site.register(models.ProductSize)
admin.site.register(models.ProductDescription)
admin.site.register(models.ProductBrands)
admin.site.register(models.ProductFavorite)
admin.site.register(models.Banner)

