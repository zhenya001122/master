from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost', 'image', 'vendor_cod', 'stock', 'category', 'status']
