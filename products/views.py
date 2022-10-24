from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from comments.forms import CommentForm
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
    comments = product_object.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product_object
            new_comment.user = request.user
            new_comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentForm()

    context = {
        'category_list': category_list,
        'product_object': product_object,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'products/products_detail.html', context)
