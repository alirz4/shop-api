from django.urls import path

from . import views

app_name = 'home_module'

urlpatterns = [
    path('users/', views.UserView.as_view(), name='users'),
    path('user-register/', views.UserRegisterView.as_view(), name='user_register'),
]