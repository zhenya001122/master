from django.urls import path, include
from rest_framework import routers

from api.blog.views import BlogViewSet
from api.products.views import ProductAPIView


router = routers.DefaultRouter()
router.register(r"blog", BlogViewSet)

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('', include(router.urls)),
]