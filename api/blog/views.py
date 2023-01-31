from rest_framework import viewsets

from api.blog.serializers import BlogSerializer
from api.permissions import IsOwnerOrReadOnly
from blog.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,)
