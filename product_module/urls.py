from django.urls import path
from rest_framework import routers

from . import views

app_name = 'product_module'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='prod-list'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='prod-detail'),
    path('edit/<int:pk>/', views.ProductEditView.as_view(), name='prod-edit'),
    path('create/', views.ProductCreateView.as_view(), name='prod-create'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='prod-delete'),
    path('favorite-prods/', views.ProductFavoriteView.as_view(), name='fave-prods'),
    path('favorite-prods/<int:pk>/', views.ProductFavoriteView.as_view(), name='fave-prods-user'),
]

router = routers.SimpleRouter()
router.register(prefix='category', viewset=views.ProductCategoryView)

urlpatterns += router.urls