from django.urls import path
from rest_framework import routers

from . import views

app_name = 'product_module'

urlpatterns = [
    # path('list/', views.ProductListView.as_view(), name='prod-list'),
    # path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='prod-detail'),
    # path('edit/<int:pk>/', views.ProductEditView.as_view(), name='prod-edit'),
    # path('create/', views.ProductCreateView.as_view(), name='prod-create'),
    # path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='prod-delete'),
    path('favorite-prods/', views.ProductFavoriteView.as_view(), name='fave-prods'),
    path('favorite-prods/<int:pk>/', views.ProductFavoriteView.as_view(), name='fave-prods-user'),
    path('new-prods/', views.NewProductsView.as_view(), name='new-prods'),
]

router = routers.SimpleRouter()
router.register(prefix='category', viewset=views.ProductCategoryViewSet)
router.register(prefix='prod-info', viewset=views.ProductInfoViewSet)
router.register(prefix='prod', viewset=views.ProductViewSet)
router.register(prefix='prod-img', viewset=views.ProductImageViewSet)
router.register(prefix='prod-desc', viewset=views.ProductDescViewSet)
router.register(prefix='prod-brand', viewset=views.ProductBrandViewSet)


urlpatterns += router.urls
