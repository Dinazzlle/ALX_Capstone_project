from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, generics, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import django_filters  # Ensure this import is present

# Serializer for registering users
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# View for user registration
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]  # Allow registration without authentication

# Filter class for product search
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    stock_available = django_filters.BooleanFilter(field_name='stock_quantity', lookup_expr='gt', method='filter_stock')

    def filter_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset

    class Meta:
        model = Product
        fields = ['name', 'category', 'price_min', 'price_max', 'stock_available']

# ViewSet for Products
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can perform CRUD on products
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ProductFilter  # Set the filter class
    ordering_fields = ['name', 'price', 'stock_quantity']
    ordering = ['name']
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ViewSet for Categories
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Require authentication to access category endpoints

# View for user login
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to access this view
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if username or password is missing
    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=400)

    # Fetch the user
    user = User.objects.filter(username=username).first()
    if not user:
        return Response({'error': 'User not found.'}, status=404)

    # Check password
    if not user.check_password(password):
        return Response({'error': 'Invalid password.'}, status=400)

    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
