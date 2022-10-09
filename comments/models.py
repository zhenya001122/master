from django.db import models
from products.models import Product


class Comment(models.Model):
    text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )
