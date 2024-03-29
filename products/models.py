from django.db import models
from orders.models import Order
from users.models import User


class Category(models.Model):
    """Модель категорий продуктов"""
    product_category = models.CharField(max_length=50, verbose_name='Категория товара',
                                        blank=True, null=True)

    def __str__(self):
        return self.product_category


class Status(models.Model):
    """Модель статуса продукта"""
    availability = models.CharField(max_length=20, verbose_name='Наличие',
                                    blank=True, null=True)

    def __str__(self):
        return self.availability


class File(models.Model):
    file = models.FileField(upload_to="files/")
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    vendor_cod = models.CharField(max_length=10)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    """Модель покупок"""
    user = models.ForeignKey(
        'users.User', related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    order = models.ForeignKey(Order, related_name='purchases', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product}, {self.cost}, {self.quantity}"

    def get_cost(self):
        return self.cost * self.quantity


class Balance(models.Model):
    """Модель баланса пользователя"""
    summ = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ваш баланс', default=10000)
    user = models.OneToOneField(
        User, related_name="balances", on_delete=models.CASCADE
    )
    purchase = models.ForeignKey(Purchase, related_name="balances", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.summ} {self.user}"
