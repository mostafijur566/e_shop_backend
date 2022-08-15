from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # status
    path('', GetStatusView.as_view()),

    # Authentication
    path('api/v1/auth/register/', RegistrationView.as_view()),
    path('api/v1/auth/login/', obtain_auth_token),

    # customer details
    path('api/v1/customer/details/', CustomerDetails.as_view()),
    path('api/v1/customer/details/<str:pk>/', CustomerDetails.as_view()),

    # Product Category
    path('api/v1/product/category/', ProductCategoriesView.as_view()),
    path('api/v1/product/category/update/<str:pk>/', ProductCategoriesView.as_view()),
]
