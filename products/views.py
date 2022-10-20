from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from products.models import Category, Product


def home(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, "base.html", context)

def products(request, category_id):
    product_list = Product.objects.filter(category=category_id)
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
        'product_list': product_list
    }
    return render(request, 'products/products_card.html', context)

def products_detail(request, id):
    category_list = Category.objects.all()
    product_object = get_object_or_404(Product, id=id)
    context = {
        'category_list': category_list,
        'product_object': product_object
    }
    return render(request, 'products/products_detail.html', context)
