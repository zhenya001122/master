from django.db import models


class Adress(models.Model):
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=20)
    flat = models.CharField(max_length=20)
