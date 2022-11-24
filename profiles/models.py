from django.db import models
from users.models import User


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    country = models.CharField(max_length=20, verbose_name='Страна')
    region = models.CharField(max_length=20, verbose_name='Область')
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=20, verbose_name='Улица')
    house = models.CharField(max_length=20, verbose_name='Дом')
    flat = models.CharField(max_length=20, blank=True, null=True, verbose_name='Квартира')

    def __str__(self):
        return f"{self.country}, {self.region}, {self.city}, {self.street}, {self.house}, {self.flat}"
