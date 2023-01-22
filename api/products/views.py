from rest_framework import generics
from products.models import Product
from api.products.serializers import ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer