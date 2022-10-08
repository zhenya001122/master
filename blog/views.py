from django.shortcuts import render, redirect

from blog.forms import BlogForm
from blog.models import Blog


def blog_add(request):
    blog = Blog.objects.all()
    if not request.user.is_authenticated:
        return redirect("/users/login")

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            Blog.objects.create(author=request.user, **form.cleaned_data)
            return redirect("blog")
    else:
        form = BlogForm()
    return render(request, "blog/blog_add.html", {"blog": blog, "form": form})
