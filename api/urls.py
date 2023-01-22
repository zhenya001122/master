from django.urls import path
from api.products.views import ProductAPIView


urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
]