from django.urls import path

from . import views

app_name = 'product_module'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='prod-list'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='prod-detail'),
    path('edit/<int:pk>/', views.ProductEditView.as_view(), name='prod-edit'),
    path('create/', views.ProductCreateView.as_view(), name='prod-create'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='prod-delete'),
]