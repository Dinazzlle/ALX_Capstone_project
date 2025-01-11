from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterView, login, ProductViewSet, CategoryViewSet

# Create a router and register ViewSets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Generate routes without 'api/' prefix
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', login, name='user-login'),
]



