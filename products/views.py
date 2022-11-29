from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from basket.forms import BasketAddProductForm
from comments.forms import CommentForm
from products.models import Category, Product, Balance, Purchase


def home(request):
    if request.user.is_authenticated:
        balance = Balance.objects.get(user=request.user.id)
        category_list = Category.objects.all()
        context = {
            'category_list': category_list,
            "balance": balance
        }
        return render(request, "base.html", context)
    else:
        category_list = Category.objects.all()
        context = {
            'category_list': category_list
        }
        return render(request, "base.html", context)


def products(request, category_id):
    product_list = Product.objects.filter(category=category_id)
    category_list = Category.objects.all()
    if request.user.is_authenticated:
        balance = Balance.objects.get(user=request.user.id)
        context = {
            'category_list': category_list,
            'product_list': product_list,
            "balance": balance
        }
        return render(request, 'products/products_card.html', context)
    else:
        context = {
            'category_list': category_list,
            'product_list': product_list,
        }
        return render(request, 'products/products_card.html', context)


def products_detail(request, product_id):
    category_list = Category.objects.all()
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentForm()
    basket_product_form = BasketAddProductForm()

    context = {
        'category_list': category_list,
        'product': product,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'basket_product_form': basket_product_form
    }
    return render(request, 'products/products_detail.html', context)


def purchases(request):
    if request.user.is_authenticated:
        purchase = Purchase.objects.filter(user=request.user.id)
        context = {
            "purchases": purchase
        }
        return render(request, "products/purchases.html", context)
