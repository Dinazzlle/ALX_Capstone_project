from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 
            'category', 'category_id', 'stock_quantity', 
            'image_url', 'created_date'
        ]

    def validate(self, data):
        if data['price'] <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        if data['stock_quantity'] < 0:
            raise serializers.ValidationError("Stock Quantity cannot be negative.")
        return data