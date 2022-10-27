from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import BlogForm
from blog.models import Blog
from comments.forms import CommentNewsForm


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


def news_detail(request, news_id):
    news = get_object_or_404(Blog, id=news_id)
    comments = news.commentnewss.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentNewsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentNewsForm()

    context = {
        'news': news,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, "blog/news_detail.html", context)
