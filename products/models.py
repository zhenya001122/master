from django.db import models
from orders.models import Order

STATUS_CHOICES = (
    ('in_stock', 'в наличии'),
    ('not_in_stock', 'нет на складе')
)


class Category(models.Model):
    power_tool = models.CharField(max_length=20, verbose_name='Электроинструмент')
    hand_tool = models.CharField(max_length=20, verbose_name='Ручной инструмент')
    household_tool = models.CharField(max_length=20, verbose_name='Хозяйственный инструмент')

class Status(models.Model):
    availability = models.CharField(max_length=20, choices=STATUS_CHOICES,
                                    verbose_name='Наличие', blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    vendor_cod = models.CharField(max_length=10)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name="products", on_delete=models.CASCADE)

class Purchase(models.Model):
    user = models.ForeignKey(
        'users.User', related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    order = models.ForeignKey(Order, related_name='purchases', on_delete=models.CASCADE)
    count = models.IntegerField()
