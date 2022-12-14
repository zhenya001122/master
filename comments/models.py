from django.db import models

from blog.models import Blog
from products.models import Product


class Comment(models.Model):
    text = models.CharField(max_length=200, verbose_name='Комментарий')
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    # def __str__(self):
    #     return self.user, self.product, self.text


class CommentNews(models.Model):
    text = models.CharField(max_length=250, verbose_name='Комментарий')
    news = models.ForeignKey(Blog, related_name="commentnewss", on_delete=models.CASCADE)
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
