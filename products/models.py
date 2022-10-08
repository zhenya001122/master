from django.db import models


class Category(models.Model):
    power_tool = models.CharField(max_length=20, verbose_name='Электроинструмент')
    hand_tool = models.CharField(max_length=20, verbose_name='Ручной инструмент')
    household_tool = models.CharField(max_length=20, verbose_name='Хозяйственный инструмент')

class Status(models.Model):
    in_stock = models.CharField(max_length=20)
    not_available = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    vendor_cod = models.CharField(max_length=10)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name="products", on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )
