"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from basket.views import basket_detail, basket_add, basket_remove
from products.views import home, products, products_detail, purchases
from orders.views import order_create
from blog.views import blog_add, news_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls')),
    path('blog/', blog_add, name='blog'),
    path('products/<int:category_id>', products, name='products'),
    path('products_detail/<int:product_id>', products_detail, name='products_detail'),
    path("news_detail/<int:news_id>", news_detail, name='news_detail'),
    path('basket_detail/', basket_detail, name='basket_detail'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_remove/<int:product_id>', basket_remove, name='basket_remove'),
    path('order_create/', order_create, name='order_create'),
    path('purchases/', purchases, name='purchases'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
