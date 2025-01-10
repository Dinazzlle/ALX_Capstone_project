import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Product Name')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains', label='Category Name')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    in_stock = django_filters.BooleanFilter(field_name='stock_quantity', lookup_expr='gt', method='filter_in_stock', label='In Stock')

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset

    class Meta:
        model = Product
        fields = ['name', 'category', 'price_min', 'price_max', 'in_stock']
